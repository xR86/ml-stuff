import sys
import os
import math

from tqdm import tqdm
import boto3

import io


class AWSSync:
	def __init__(self, bucket='bucketname', root='FolderName/', aws_access_key_id = '', aws_secret_access_key = ''): 
		print('Workspace is being initialized ...')
		 
		self.__s3_client = boto3.client('s3',\
			aws_access_key_id = aws_access_key_id,\
			aws_secret_access_key = aws_secret_access_key )
		self.__bucket = bucket
		self.__root = root
		
		print('\t__root      = %s' % self.__root)
		print('\t__s3_client = %s' % self.__s3_client)
	
	def sync_notebook_s3(self, filenames, update=False):
		s3_path = [self.__root + fn[i] for i in range(len(fn))]
		# for i in range(len(filenames)):
		#     s3_path.append(self.__root + filenames[i])
		
		for i in range(len(filenames)):
			try:
				self.__s3_client.head_object(Bucket = self.__bucket, Key = s3_path[i])
				print('Path found on S3 ! Skipping %s...' % s3_path[i])
				if update:
					print('Sync with update, trying to delete object ...')
					try:
						self.__s3_client.delete_object(Bucket = self.__bucket, Key = s3_path[i])
					except:
						print('Unable to delete %s...' % s3_path[i])
					else:
						print('File should be deleted, Uploading %s...' % s3_path[i])
						self.__s3_client.upload_file(filenames[i], self.__bucket, s3_path[i])
			except:
				# add tqdm
				print('File doesn\'t exist, Uploading %s...' % s3_path[i])
				self.__s3_client.upload_file(filenames[i], self.__bucket, s3_path[i])


# functions that could be runned separately
# some architecture decisions to be made
def hook(t):
	def inner(bytes_amount):
		t.update(bytes_amount)
	return inner

def convert_size1(size_bytes):
	if size_bytes == 0:
		return "0B"
	size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
	i = int(math.floor(math.log(size_bytes, 1024)))
	p = math.pow(1024, i)
	s = round(size_bytes / p, 2)
	return "%s %s" % (s, size_name[i])

def file_download(fd_bucket, fd_key, fd_fname):
	file_obj = s3_client.get_object(Bucket=fd_bucket, Key=fd_key)
	file_size = file_obj['ContentLength']#.content_length
	print('File size is: %s' % file_size)
	print(convert_size1(int(file_size)))
	with tqdm(total=file_size, unit='B', unit_scale=True, desc=fd_fname) as t:
		s3_client.download_file(\
			Filename=fd_fname,\
			Bucket=fd_bucket,\
			Key=fd_key,\
			Callback=hook(t))





if __name__ == "__main__":
	ws = AWSSync()

	filenames = [\
		'EDA.ipynb',\
		'Sync.ipynb',\
		'proc.csv'\
	]

	ws.sync_notebook_s3(filenames)

	# vs
	s3_client = boto3.client('s3',\
		aws_access_key_id = '',\
		aws_secret_access_key = '' )

	file_download(fd_bucket='datatest', fd_key='DS/2017.csv', fd_fname='2017.csv')

