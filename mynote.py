"""
WebApp - MyNotes
Programmer - Mr.( ;D ) Aditya Gupta {AdiG15}

Inspired by ANotePad.com

FUTURE tags - 'FUTURE (Suspected_level_of_implementing)'... as of now the suspected levels are signified by these-
				.   -> Easy
				..	-> Can't Say(But, Medium)
				*	-> May be Difficult

Notes - User_id and User-name have been used for the same thing... later pick one of them
"""

from flask import Flask, render_template, request
import sqlite3

global __login__
global __user_exist
global __user_name
global __user_id

__login__ = False
__user_exist = False	#Doesn't already exist
__user_name = 'Login'
__user_id = 'AdiG15'

app = Flask(__name__)

#'credentials' database will store u_id and pwd
#'notes' database will store notes, and will link to the particular user_id

def create_connection(db_name):
	l = []
	conn = sqlite3.connect(db_name)
	l.append(conn)
	l.append(conn.cursor())
	return l  #l[0] is the connection, and l[1] is the cursor object

def close_connection(conn):
	conn.close()

def check_user_exist(db_conn, db_cur, u_id):
	#Checks if there exists a table named $u_id, and returns true if yes, it exists
	return False

def add_user_cred(cred_list):	#requires cursor object, and a table name, and list of credentials (3 thins:u_id, email and password)
	db_conn = sqlite3.connect('credentials.db')
	db_cur = db_conn.cursor()
	db_cur.execute("CREATE TABLE IF NOT EXISTS user_cred (u_id TEXT, email TEXT, pass_wd TEXT)")
	db_cur.execute("INSERT INTO user_cred VALUES ('" + cred_list[0] + "', '" + cred_list[1] + "', '" + cred_list[2]+ "') ")
#	db_cur.execute("INSERT INTO user_cred VALUES ('AdiG15", "ag15035", "Adi')")
	db_conn.commit()
	db_conn.close()

def addnote(u_id, note):	#note will be a list of 2 elements : note_heading and note_content
	#FUTURE (.) - Remove the u_id column for every note... instead, try to get that from the table_name
	db_conn = sqlite3.connect('notes.db')
	db_cur = db_conn.cursor()
	db_cur.execute("CREATE TABLE IF NOT EXISTS '" + u_id + "' (u_id TEXT, note_heading TEXT, note_content TEXT)")
	db_cur.execute("INSERT INTO '" + u_id + "' VALUES ('" + u_id + "', '" + note[0] +  "', '" + note[1]+ "')")
	db_conn.commit()
	db_conn.close()

#cred_conn, cred_cur = create_connection('credentials.db')
#note_conn, note_cur = create_connection('notes.db')

#add_user_cred(["AdiG15", "ag15035@gmail.com", "Adi@15"])

def get_ip():
	#get the ip_addr here
	ip_addr = '443.234.45.3'
	return ip_addr

@app.route('/')
def index():
	if __login__ == False:
		__user_id = get_ip();
		return render_template('index.html')
	elif __login__ == True:
		return render_template('index.html')

@app.route('/login')
def login():
	return render_template('login.html')

@app.route('/add_note', methods = ['POST'])
def add_note_to_db():
	note_head = request.form['Heading']
	note_cont = request.form['Note_Area']
	addnote(__user_id, [note_head, note_cont])
	return "Note Added"

@app.route('/register')
def register():
	return render_template('register.html')

@app.route('/check_user', methods = ['POST'])
def check_user():
	#FUTURE (..) - Add functionality that the user can enter either of his email, or user_id (One possible way is to 1st search the u_id in user_id and then in email_id columns)
	u_id = request.form['user_name']
	passwd = request.form['password']
	#Check here if it exists or not
	global __login__
	__login__ = True #Just bypassed for now
	if __login__ == True:
		return index()
	elif __login__ == False:
		return login()

if __name__ == "__main__":
	app.run( debug = "True")