import sqlite3
conn = sqlite3.connect('example.db')

c = conn.cursor()

print('\n\n*****location table****\n')
'''
for row in c.execute('SELECT * FROM location'):
	# print(c.fetchall())
	print(row)
'''
'''
c.execute('SELECT * FROM location')
print(c.fetchall())
'''
c.execute('SELECT * FROM location')
copy = c.fetchall()
for row in copy:
	print row


print('\n\n*****files table****\n')
c.execute('SELECT * FROM files')
copy = c.fetchall()
for row in copy:
	print row

print('\n\n*****file_info table****\n')
c.execute('SELECT * FROM file_info')
copy = c.fetchall()
for row in copy:
	print row

conn.close()