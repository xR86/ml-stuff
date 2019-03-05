import datetime as dt
import sys

import zmq

from utils import convert_size, dump_to_csv, parseSize, row_print, utf8len


def zeromq_server():
	context    = zmq.Context()
	subscriber = context.socket(zmq.SUB)
	subscriber.connect("tcp://localhost:5563")
	subscriber.setsockopt(zmq.SUBSCRIBE, b"emails")

	cnt = 0
	running_bytes = 0
	server_start = dt.datetime.now()

	while True:
		# envelope + data
		[address, data] = subscriber.recv_multipart()
		running_bytes += len(data)
		cnt += 1

		row_data = (
			(dt.datetime.now() - server_start),
			convert_size(running_bytes),
			cnt # "{:,}".format(cnt)
		)
		print(row_print('ZeroMQ', 'single', 'single node',row_data))

		# print('ZeroMQ - single node - %s - %s - %s messages' % (
		# 		(dt.datetime.now() - client_start),
		# 		convert_size(running_bytes),
		# 		"{:,}".format(cnt)
		# 	))

		if data == b'END':
			dump_to_csv('server', 'ZeroMQ', 'localhost', 'single', 'single node', row_data)
			sys.exit()

	subscriber.close()
	context.term()


if __name__ == "__main__":
	zeromq_server()
