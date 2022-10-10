import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('index.html', posts=posts)

@app.route('/act1')
def act1():
    return render_template('act1.html')

@app.route('/act2')
def act2():
    return render_template('act2.html')

@app.route('/act5')
def act5():
    return render_template('act5.html')

app.run(host="localhost", debug=True)
