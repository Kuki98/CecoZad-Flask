#!/home/pr0phet/anaconda3/bin/python3
from flask import Flask, request, render_template
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="navi98%",
    database="DB_work"
)
cursor = db.cursor()

app = Flask(__name__)

@app.route('/')
def index():
	query= 'SELECT comment FROM commentsTable'
	cursor.execute(query)
	return render_template('static_page.html', names=cursor)

@app.route('/hello/')
def hello():
	query = 'SELECT comment FROM commentsTable'
	cursor.execute(query)
	return render_template('hello.html', names=cursor)

@app.route('/login', methods=['POST', 'GET'])
def login():
	if request.method == 'POST':
		return do_the_login()
	else:
		return show_the_login_form()
		
def do_the_login():
	return '<!DOCTYPE html>\
	<html>\
	<head>\
		<title></title>\
	</head>\
	<body>\
	<p> ACCESS GRANTED </p>\
	</body>\
	</html>'

def show_the_login_form():
	return '<!DOCTYPE html>\
	<html>\
	<head>\
		<title></title>\
	</head>\
	<body>\
		<form method="POST">\
			<input type="text" name="username"><br>\
			<input type="password" name="password">\
			<input type="submit" name="submit">\
		</form>\
	</body>\
	</html>'
