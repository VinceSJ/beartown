import sqlite3 as sq3

conn = sq3.connect('db/bears.db')
curs = conn.cursor()
# Start the table if it does not already exist.
curs.execute('''CREATE TABLE IF NOT EXISTS bears
(id INT PRIMARY KEY,
name VARCHAR(50),
species VARCHAR(50),
age INT,
weight FLOAT,
gender VARCHAR(10),
furcolor VARCHAR(50),
inrelationship BIT,
bio VARCHAR(1000))''')
# Notes on use:
#   'id' used for referencing bear, also to grab profile pic
#   Most strings have a maxlength of 50 chars.
#   'gender' has a maxlength of 10, should only have three values: 'male', 'female', 'nonbinary'
#   'inrelationship' is a bit field: 0 means currently single, 1 means in a relationship
#   'bio' field has a maxlength of 1000, so need to cap form entry accordingly.

insertstructure = 'INSERT INTO bears (id, name, species, age, weight, gender, furcolor, inrelationship, bio) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)'


n = 4   # testing, kill soon
test = (n, 'Test' + str(n), 'Species', 100, 80.2, 'male', 'orange', 0, "He's a figment of your imagination. I'm sorry.")
curs.execute(insertstructure, test)
conn.commit()

curs.execute('SELECT id, name FROM bears')
rows = curs.fetchall()
print(rows)