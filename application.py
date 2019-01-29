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

