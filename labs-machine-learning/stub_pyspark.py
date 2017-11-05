import os
import webbrowser

os.environ['PYSPARK_PYTHON'] = '/usr/bin/python3'
os.environ['SPARK_HOME'] = '/opt/spark'
print('PYSPARK_PYTHON = %s' % os.environ['PYSPARK_PYTHON'])
print('SPARK_HOME = %s' % os.environ['SPARK_HOME'])


from pyspark import *
sc = SparkContext('local', 'App Name', pyFiles=['README.md'])
#sc = SparkContext('spark://10.0.2.15', 'pyspark') #4040 / 7077



if __name__ == '__main__':
	webbrowser.open_new_tab('http://127.0.0.1:4040')

	print('\n' + '######' * 3 + '\n') 

	# spark = SparkSession\
	# .builder\
	# .appName("PythonWordCount")\
	# .getOrCreate()


	textFile = sc.textFile('README.md')

	print('count: %i' % textFile.count())
	print('first item: \'%s\'' % textFile.first())

	words = textFile.flatMap(lambda x: x.split(' '))
	word_count = (
	  words.map(lambda x: (x, 1))
	.reduceByKey(lambda x, y: x+y))
	output = word_count.collect()

	# # print('words: %s' % words)
	# # print('word_count: %s' % word_count)

	# print(output)

	# # for (word, count) in output:
	# # print("%s: %i" % (word, count))

	# print()
	# while 1:
	# 	wait = input("PRESS ENTER TO CONTINUE.")
	# 	if wait == '':
	# 		exit()