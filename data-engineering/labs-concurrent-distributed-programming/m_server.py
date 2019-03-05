from config import CONFIG
# import b_udp_s

'''Main script to run test battery

More links here:
+ https://users.pja.edu.pl/~jms/qnx/help/watcom/clibref/src/spawn.html
+ https://docs.python.org/3/library/subprocess.html#replacing-the-os-spawn-family
+ https://stackoverflow.com/questions/16450788/python-running-subprocess-in-parallel
'''
import sys
import subprocess

if __name__ == '__main__':
	print(CONFIG['demo_battery'])

	# # blocking
	# proc = subprocess.Popen([sys.executable, 'b_udp_c.py'])
	# proc.communicate()

	# # non-blocking
	# # pid = os.spawnlp(os.P_NOWAIT, sys.executable, 'b_udp_c.py')
	# pid = subprocess.Popen([sys.executable, 'b_udp_s.py']).pid

	print(('===' * 10) + 'b_udp_s' + ('===' * 10))

	pid = subprocess.Popen([sys.executable, 'b_udp_s.py']).pid
	pid = subprocess.Popen([sys.executable, 'b_udp_c.py']).pid
	
	print(('===' * 10) + 'b_udp_s' + ('===' * 10))
	