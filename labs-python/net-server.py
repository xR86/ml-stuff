#!/usr/bin/python

import socket

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.

# Simple iterative server
# 
# Alternative 1 -> try-catch with raise
'''
while True:
	try:
		c, addr = s.accept()		# Establish connection with client.
		print 'Got connection from', addr
		# print '  name: ', c.recv()
		c.send('Thank you for connecting')
		c.close()					# Close the connection
	except (KeyboardInterrupt, SystemExit): #one issue though - exception is stored and raised at the end of the loop !
		raise
		exit()
'''

# Alternative 2 -> try-catch with signal capturing
# possible issue in 2.7: https://mail.python.org/pipermail/python-list/2015-September/696407.html
import signal,sys,time
terminate = False

def signal_handling(signum,frame):
	#global terminate
	#terminate = True
	print('You pressed Ctrl+C!')
	sys.exit(0)

signal.signal(signal.SIGINT,signal_handling)

while True:
	c, addr = s.accept()		# Establish connection with client.
	print 'Got connection from', addr
	message = c.recv(1024)
	print '  name: ', message
	c.send('Thank you for connecting, ' + message)
	c.close()					# Close the connection
	if terminate:
		print "Graceful shutdown ..."
		break
