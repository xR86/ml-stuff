
def bytes_len(byte):
	return len(byte)

def utf8len(s):
	return len(s.encode('utf-8'))

import math

def convert_size(size_bytes):
	if size_bytes == 0:
		return "0B"
	size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
	i = int(math.floor(math.log(size_bytes, 1024)))
	p = math.pow(1024, i)
	s = round(size_bytes / p, 2)
	return "%s %s" % (s, size_name[i])


units = {"B": 1, "KB": 10**3, "MB": 10**6, "GB": 10**9, "TB": 10**12}

def parseSize(size):
	number, unit = [string.strip() for string in size.split()]
	return int(float(number)*units[unit])


def dump_to_csv(suffix, protocol, location='localhost', setup='single', mode='single', row_data=['', '', '']):
	with open('data/metadata_%s_%s.csv' % (suffix, protocol), 'w+') as md:
		md.write('Protocol,Location,Setup,Mode,Time,Size(MB),Count\n')
		md.write(
			'%s,%s,%s,%s' % (protocol, location, setup, mode) + \
			',%s,%s,%s\n' % row_data)

# import signal
# import sys
# # def signal_handler(sig, frame):
# # 	print('You pressed Ctrl+C!')
# # 	sys.exit(0)

# # signal.signal(signal.SIGINT, signal_handler)

def row_print(protocol, setup, mode, row_data):
	return '%s - %s - %s' % (protocol, setup, mode) + \
			' - %s - %s - %s messages' % row_data

