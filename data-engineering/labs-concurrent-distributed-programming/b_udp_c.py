import datetime as dt
import socket
import sys
from utils import convert_size, dump_to_csv, parseSize, row_print, utf8len


def udp_client_single_node(lim='10 MB'):
	UDP_IP = '127.0.0.1'
	UDP_PORT = 5005

	sock = socket.socket(
		socket.AF_INET,
		socket.SOCK_DGRAM
	)

	cnt = 0
	running_bytes = 0
	client_start = dt.datetime.now()
	
	with open('data/emails.csv') as fd:
		for line in fd:
			if running_bytes <= parseSize(lim):
				# print('%s - %s bytes' % (line, utf8len(line)))
				line_bytes = line.encode('utf-8')
				sock.sendto(line_bytes, (UDP_IP, UDP_PORT))
			else:
				sock.sendto('END'.encode('utf-8'), (UDP_IP, UDP_PORT))

				dump_to_csv('client', 'UDP', 'localhost', 'single', 'single node', row_data)
				sys.exit()

			cnt += 1
			running_bytes += utf8len(line)

			row_data = (
				(dt.datetime.now() - client_start),
				convert_size(running_bytes),
				cnt # "{:,}".format(cnt)
			)
			print(row_print('UDP', 'single', 'single node',row_data))


if __name__ == '__main__':
	udp_client_single_node()
