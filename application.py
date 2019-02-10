#!/home/pr0phet/anaconda3/bin/python3
from flask import Flask, request, render_template, redirect, url_for
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
@app.route('/index')
def index():
	query="SELECT img_path, img_name\
			FROM imageTable"
	cursor.execute(query)
	return render_template('index.html', images=cursor)

@app.route('/<pic_name>')
def view_comment(pic_name):
	query= 'SELECT comment, comment_id, img_id\
			FROM commentsTable'
	cursor.execute(query)
	return render_template('static_page.html', names=cursor, pic_name=pic_name)

@app.route('/submit_comment/<pic_name>', methods=['POST', 'GET'])
def submit_comment(pic_name=None):
	#get comment and insert into base
	if request.method == 'POST':
		query = "INSERT INTO commentsTable(comment, img_id)\
				VALUES('%s', '%s')" % (request.form['comment'], request.form['image-id'])
		cursor.execute(query)
		db.commit()
		return redirect(url_for('view_comment', pic_name=pic_name))

@app.route('/delete_comment/<pic_name>', methods=['POST', 'GET'])
def delete_comment(pic_name=None):
	if request.method == 'POST':
		query = "DELETE FROM commentsTable\
				WHERE comment_id = '%s'" % request.form['delete_comment']
		cursor.execute(query)
		db.commit()
		return redirect(url_for('view_comment', pic_name=pic_name))

@app.route('/edit_comment/<pic_name>', methods=['POST', 'GET'])
def edit_comment(pic_name=None):
	edit_value = request.form['edit_comment']	
	return render_template('edit_page.html', edit_value=edit_value)

@app.route('/update_comment/<pic_name>', methods=['POST', 'GET'])
def update_comment(pic_name=None):
	if request.method == 'POST':
		query = "UPDATE commentsTable\
					SET comment = '%s'\
					WHERE comment_id = '%s' " % (request.form['new_comment'], request.form['edit_value'])
		cursor.execute(query)
		db.commit()
	return redirect(url_for('view_comment', pic_name=pic_name))
