import datetime as dt
import time
import sys

import zmq

from utils import convert_size, dump_to_csv, parseSize, row_print, utf8len


def zeromq_client(lim='10 MB'):
	context   = zmq.Context()
	publisher = context.socket(zmq.PUB)
	publisher.bind("tcp://*:5563")


	cnt = 0
	running_bytes = 0
	client_start = dt.datetime.now()
	
	with open('data/emails.csv') as fd:
		for line in fd:
			running_bytes += utf8len(line)
			cnt += 1

			row_data = (
				(dt.datetime.now() - client_start),
				convert_size(running_bytes),
				cnt # "{:,}".format(cnt)
			)

			if running_bytes <= parseSize(lim):
				# print('%s - %s bytes' % (line, utf8len(line)))
				line_bytes = line.encode('utf-8')
				
				# envelope + content
				publisher.send_multipart([b'emails', line_bytes])
			else:
				publisher.send_multipart([b'emails', 'END'.encode('utf-8')])
				dump_to_csv('client', 'ZeroMQ', 'localhost', 'single', 'single node', row_data)
				sys.exit()

			print('ZeroMQ - single node - %s - %s - %s messages' % (
				(dt.datetime.now() - client_start),
				convert_size(running_bytes),
				"{:,}".format(cnt)
			))

	publisher.close()
	context.term()


if __name__ == "__main__":
	zeromq_client()
