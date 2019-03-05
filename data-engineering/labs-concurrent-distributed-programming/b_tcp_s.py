import socket
import sys


def tcp_server_single_node(lim='10 MB'):
	TCP_IP = 'localhost'
	TCP_PORT = 10000

	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	server_address = (TCP_IP, TCP_PORT)
	# print('starting up on {} port {}'.format(*server_address))
	sock.bind(server_address)
	sock.listen(1)


	while True:
		connection, client_address = sock.accept()
		try:
			print('connection from', client_address)

			while True:
				data = connection.recv(16)
				print('received {!r}'.format(data))
				if data:
					print('sending data back to the client')
					connection.sendall(data)
				else:
					print('no data from', client_address)
					break

		finally:
			connection.close()


if __name__ == '__main__':
	tcp_server_single_node()
