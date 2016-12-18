import sqlite3
conn = sqlite3.connect('example.db')

c = conn.cursor()


import os
import hashlib
import time

def get_file_md5(filePath):
	h = hashlib.md5()
	h.update(open(filePath,"rb").read())
	return h.hexdigest()

def get_file_sha256(filePath):
	h = hashlib.sha256()
	h.update(open(filePath,"rb").read())
	return h.hexdigest()


def get_dir_data(dir_path):
	dir_path = os.path.realpath(dir_path)
	
	#print next(os.walk(dir_path))[2]
	#print os.path.basename(dir_path)
	
	id_location = 0
	id_file = 0
	for dir_file in next(os.walk(dir_path))[2]:
		file_name = dir_file
		file_md5 = get_file_md5(dir_file)
		file_sha256 = get_file_sha256(dir_file)
		file_size = os.path.getsize(dir_file)
		
		file_time = time.gmtime(os.path.getctime(dir_file))
		file_formatted_time = time.strftime("%Y-%m-%d %I:%M:%S %p", file_time)
		file_path = os.path.realpath(dir_file)
		

		location_values = (id_location, file_path)
		c.execute("INSERT INTO location VALUES (?, ?)", location_values)

		files_values = (id_location, id_file)
		c.execute("INSERT INTO files VALUES (?, ?)", files_values)

		file_info_values = (id_file, file_name, file_size, file_formatted_time, file_md5)
		c.execute("INSERT INTO file_info VALUES (?, ?, ?, ?, ?)", file_info_values)

		id_location += 1
		id_file += 1


get_dir_data('./')

# Save (commit) the changes
conn.commit()

conn.close()