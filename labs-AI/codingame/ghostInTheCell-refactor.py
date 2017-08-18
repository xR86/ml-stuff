import sys
import math


class AI:
	def __init__(self):
		self.FACTORY_NEIGHBORS = {}
		self.FACTORY = {}
		self.ENTITIES = {}
		self.BOMBS = {}

		self.turns = 0
		self.bombs_count = 2

	# -- input --
	def read_neighbors(self):   
		'''
		one time functions (is read at the start of the match)
		''' 	
		factory_count = int(input())  # the number of factories
		link_count = int(input())  # the number of links between factories
		for i in range(link_count):
			factory_1, factory_2, distance = [int(j) for j in input().split()]
			# print(factory_1, factory_2, distance, file=sys.stderr)
			
			if factory_1 not in self.FACTORY_NEIGHBORS:
				self.FACTORY_NEIGHBORS[factory_1] = {}
			self.FACTORY_NEIGHBORS[factory_1][factory_2] = distance
		#print(FACTORY_NEIGHBORS, file=sys.stderr)

	def read_factory_entities(self):
		# TODO: should accomodate history for this, instead of reset
		# on new round
		self.FACTORY = {}
		self.ENTITIES = {}
		self.BOMBS = {}
		
		entity_count = int(input())  # the number of entities (e.g. factories and troops)
		for i in range(entity_count):
			entity_id, entity_type, arg_1, arg_2, arg_3, arg_4, arg_5 = input().split()
			entity_id = int(entity_id)
			
			if entity_type == "FACTORY":
				self.FACTORY[entity_id] = {}
				self.FACTORY[entity_id]["owner"] = int(arg_1)
				self.FACTORY[entity_id]["count"] = int(arg_2)
				self.FACTORY[entity_id]["gen"] 	 = int(arg_3)
			elif entity_type == "TROOP":
				self.ENTITIES[entity_id] = {}
				self.ENTITIES[entity_id]["owner"] 		= int(arg_1)
				self.ENTITIES[entity_id]["origin"]		= int(arg_2)
				self.ENTITIES[entity_id]["destination"]	= int(arg_3)
				self.ENTITIES[entity_id]["count"]		= int(arg_4)
				self.ENTITIES[entity_id]["time_left"] 	= int(arg_5)
			else:
				self.BOMBS[entity_id] = {}
				self.BOMBS[entity_id]["owner"] 		= int(arg_1)
				self.BOMBS[entity_id]["origin"]		= int(arg_2)
				self.BOMBS[entity_id]["destination"]= int(arg_3)
				self.BOMBS[entity_id]["time_left"]	= int(arg_4)

		# print(FACTORY, file=sys.stderr)
		# print(ENTITIES, file=sys.stderr)
		# print(BOMBS, file=sys.stderr)


	# *****Core heuristics*****
	def choose(self):
		current_factory = self.mark_current(1)
		print('current_fact = ', current_factory, file=sys.stderr)
		current_enemy_factory = self.mark_current(-1)
		print('current_enemy_fact = ', current_enemy_factory, file=sys.stderr)

		mean_troops = self.get_mean()
		print('mean_troops = ', mean_troops, file=sys.stderr)
		
		# SPREAD strategy - attacks multiple factories (divides main troop)
		if self.turns == 0: #or: current_factory count > mean !!!
			att_factories = self.calculate_multiple_closest_smaller(current_factory)
			print('closest_fact = ', att_factories, file=sys.stderr)
			if not att_factories:
				print("WAIT")

			if current_enemy_factory > mean_troops and self.bombs_count > 0:
				print("BOMB " + 
						str(current_factory) + " " +   # source
						str(current_enemy_factory),     # destination
						end=';')
				self.bombs_count -= 1

			else:
				for i in range(len(att_factories)):
					print("MOVE " + 
						str(current_factory) + " " + # source
						str(att_factories[i][0])   + " " + # destination
						str(att_factories[i][2]), 
						end=';')
					if i+1 == len(att_factories):
						print('MSG good luck')
		# SAFE strategy - only attacks closest (maintains a main troop)
		else:
			closest_factory, count = self.calculate_closest_smaller(current_factory)
			print('closest_fact = ', closest_factory, count, file=sys.stderr)
			
			if closest_factory == -1:
				print("WAIT")
			else:
				print("MOVE " + 
					str(current_factory) + " " + # source
					str(closest_factory)   + " " + # destination
					str(count) )

	# **Utils**
	def mark_current(self, player):
		'''
		Shows the current factory / troop of the user
		current = the one with the most troops of the user
		'''
		max_count = -1
		entity_max_id = -1
		for i in range(len(self.FACTORY)):
			if self.FACTORY[i]['count'] > max_count and self.FACTORY[i]['owner'] == player:
				max_count = self.FACTORY[i]['count']
				entity_max_id = i

		return entity_max_id

	def get_mean(self):
		'''
		Returns the mean of troops from all players
		'''
		sum = 0.0
		n = len(self.FACTORY)

		for i in range(n):
			sum += self.FACTORY[i]['count']

		return sum / n

	'''
	def mark_first_n_current(self, n):
		max_count = -1
		entity_max_id_list = []
		entity_max_id = -1
		for i in range(len(self.FACTORY)):
			if self.FACTORY[i]['count'] > max_count and self.FACTORY[i]['owner'] == 1:
				max_count = self.FACTORY[i]['count']
				entity_max_id = i

		return entity_max_id_list

	'''

	# **Capture heuristics**
	def calculate_closest_smaller(self, current_factory):
		'''
		Attacks closest factory that doesn't belong to the user
		'''
		min_dist = 10000
		entity_max_id = -1
		max_count = 0

		if current_factory in self.FACTORY_NEIGHBORS:
			for neighbor in self.FACTORY_NEIGHBORS[current_factory].items():
				#print('neigh: ', neighbor, file=sys.stderr)
				#print(FACTORY_NEIGHBORS[current_factory])
				if neighbor[1] < min_dist and \
								self.FACTORY[current_factory]['count'] > self.FACTORY[neighbor[0]]['count'] + 1:
					min_dist = neighbor[1]
					max_count = self.FACTORY[neighbor[0]]['count']
					entity_max_id = neighbor[0]

		#return (entity_max_id, troops_gen * distance + troops_def)
		return (entity_max_id, max_count)

	def calculate_multiple_closest_smaller(self, current_factory):
		'''
		Attacks closest factory that doesn't belong to the user
		'''
		factories_smaller_temp = []
		factories_smaller = []

		entity_id = -1
		distance = -1
		att_count = -1

		sum_count = 0

		if current_factory in self.FACTORY_NEIGHBORS:
			for neighbor in self.FACTORY_NEIGHBORS[current_factory].items():
				#print('neigh: ', neighbor, file=sys.stderr)
				#print(FACTORY_NEIGHBORS[current_factory])
				if self.FACTORY[current_factory]['count'] > self.FACTORY[neighbor[0]]['count'] + 1:
					entity_id = neighbor[0]
					distance = neighbor[1]
					att_count = self.FACTORY[neighbor[0]]['count'] + 1

					factories_smaller_temp.append( (entity_id, distance, att_count) )

		if factories_smaller_temp: #if list is not empty
			i = 0
			factories_smaller_temp = sorted(factories_smaller_temp, key=lambda fact: fact[1])
			#print('factories_smaller_temp = ', factories_smaller_temp, ', ', len(factories_smaller_temp), file=sys.stderr)
			while sum_count < self.FACTORY[current_factory]['count'] and i < len(factories_smaller_temp):
				#print('factories_smaller_temp[', i, '] = ', factories_smaller_temp[i], file=sys.stderr)
				factories_smaller.append( factories_smaller_temp[i] )

				sum_count += factories_smaller_temp[i][2]
				i += 1
		
		return factories_smaller

	# end class AI

# -----
# MAIN
# -------------------------

AI = AI()
AI.read_neighbors()

# game loop
while True:
	AI.read_factory_entities()

	AI.choose()
