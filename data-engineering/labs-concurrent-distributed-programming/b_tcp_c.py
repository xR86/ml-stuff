import socket
import sys


def tcp_client_single_node(lim='10 MB', rounds = 0):
	TCP_IP = 'localhost'
	TCP_PORT = 10000

	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	server_address = (TCP_IP, TCP_PORT)
	# print('connecting to {} port {}'.format(*server_address))
	sock.connect(server_address)

	try:
		message = b'This is the message.  It will be repeated.'
		print('sending {!r}'.format(message))
		sock.sendall(message)

		# Look for the response
		amount_received = 0
		amount_expected = len(message)

		while amount_received < amount_expected:
			data = sock.recv(16)
			amount_received += len(data)
			print('received {!r}'.format(data))

	finally:
		print('closing socket')
		sock.close()


if __name__ == '__main__':
	tcp_client_single_node(rounds = 1)

	# for i in range(3)
	# 	tcp_client_single_node(rounds = i+1)
