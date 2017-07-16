import flask
import sqlite3 as sq3

conn = sq3.connect('db/bears.db')  # Connect to db
curs = conn.cursor()  # Cursor for db interaction.

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

insertstructure = 'INSERT INTO bears (id, name, species, age, weight, gender, furcolor, inrelationship, bio) \
 VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)'
# Structure for creating inserts. Pass new objects as tuples matching accordingly.

# curs.execute(insertstructure, thingbeinginserted)

app = flask.Flask(__name__)


@app.route('/')
def home():
    conn = sq3.connect('db/bears.db')  # Connect to db
    curs = conn.cursor()  # Cursor for db interaction.
    # Grab bear info:
    curs.execute('SELECT id, name FROM bears')
    twocolrows = curs.fetchall()  # Returns list of tuples with id, name. Used in template
    return flask.render_template('mainpage.html', bearlist=twocolrows)


app.run(port=8000, debug=True)
