import sqlite3
conn = sqlite3.connect('example.db')

c = conn.cursor()

# Create table
c.execute('''CREATE TABLE location
             (id_location text, location text)''')

c.execute('''CREATE TABLE files
             (id_location text, id_file text)''')

c.execute('''CREATE TABLE file_info
             (id_file text, file_name text, file_size text, creation_time text, file_md5 text)''')

# Save (commit) the changes
conn.commit()

# Close the connection
# => any change that has not been commited will be lost
conn.close()