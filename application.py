#!/home/pr0phet/anaconda3/bin/python3
import sys

from flask import Flask, request, render_template, redirect, url_for
import mysql.connector
import os

app_path = os.getcwd()
images_path = '/static/uploads/'
db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="kuki",
)
cursor = db.cursor()

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    query = "SELECT id, path, name FROM images"
    cursor.execute(query)
    return render_template('index.html', images=cursor)


@app.route('/<pic_id>')
def view_comment(pic_id):
    query = "SELECT id, path, name FROM images WHERE id = " + pic_id + ' LIMIT 1';
    cursor.execute(query)
    image = cursor.fetchone()
    query = 'SELECT c.comment, c.id FROM comments c WHERE c.image_id = ' + pic_id
    cursor.execute(query)
    return render_template('view_image.html', comments=cursor, image=image)


@app.route('/submit_comment/<pic_id>', methods=['POST', 'GET'])
def submit_comment(pic_id):
    # get comment and insert into base
    if request.method == 'POST':
        query = "INSERT INTO comments(comment, image_id)\
                    VALUES('%s', '%s')" % (request.form['comment'], pic_id)
        cursor.execute(query)
        db.commit()
        return redirect(url_for('view_comment', pic_id=pic_id))


@app.route('/delete_comment/<pic_id>', methods=['POST', 'GET'])
def delete_comment(pic_id=None):
    if request.method == 'POST':
        query = "DELETE FROM comments WHERE id = '%s'" % request.form['delete_comment']
        cursor.execute(query)
        db.commit()
        return redirect(url_for('view_comment', pic_id=pic_id))


@app.route('/edit_comment/<pic_id>', methods=['POST', 'GET'])
def edit_comment(pic_id=None):
    edit_value = request.form['edit_comment']
    return render_template('edit_comment.html', edit_value=edit_value, pic_id=pic_id)


@app.route('/update_comment/<pic_name>', methods=['POST', 'GET'])
def update_comment(pic_name=None):
    if request.method == 'POST':
        query = "UPDATE comments\
                    SET comment = '%s'\
                    WHERE comment_id = '%s' " % (request.form['new_comment'], request.form['edit_value'])
        cursor.execute(query)
        db.commit()
    return redirect(url_for('view_comment', pic_name=pic_name))


@app.route('/upload_file', methods=['POST', 'GET'])
def upload_file():

    if request.method == 'POST':
        f = request.files['image_upload']
        if f.filename != '':
            f.save(app_path + images_path + f.filename)
            query = "INSERT INTO images(path, name)\
                    VALUES('%s', '%s')" % ((images_path + f.filename), (f.filename))
            cursor.execute(query)
            db.commit()
    return redirect(url_for('index'))
