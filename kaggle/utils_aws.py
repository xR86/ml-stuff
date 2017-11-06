import boto3


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


if __name__ == "__main__":
	ws = AWSSync()

	filenames = [\
		'EDA.ipynb',\
		'Sync.ipynb',\
		'proc.csv'\
	]

	ws.sync_notebook_s3(filenames)