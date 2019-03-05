import datetime as dt
import signal
import socket
import sys

from utils import bytes_len, convert_size, dump_to_csv, row_print


def udp_server_single_node(lim='10MB'):
	UDP_IP = '127.0.0.1'
	UDP_PORT = 5005

	sock = socket.socket(
		socket.AF_INET,
		socket.SOCK_DGRAM
	)
	sock.bind((UDP_IP, UDP_PORT))

	cnt = 0
	running_bytes = 0
	server_start = dt.datetime.now()

	while True:
		signal.signal(signal.SIGINT, signal.default_int_handler)
		try:
			data, addr = sock.recvfrom(65535)
			running_bytes += len(data)
			cnt += 1

			row_data = (
				(dt.datetime.now() - server_start),
				convert_size(running_bytes),
				cnt # "{:,}".format(cnt)
			)
			print(row_print('UDP', 'single', 'single node',row_data))

			if data == b'END':
				dump_to_csv('server', 'UDP', 'localhost', 'single', 'single node', row_data)
				sys.exit()

		except KeyboardInterrupt:
			dump_to_csv('server', 'UDP', 'localhost', 'single', 'single node', row_data)
			sys.exit()


if __name__ == '__main__':
	udp_server_single_node()
