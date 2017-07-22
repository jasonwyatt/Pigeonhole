import os
import sqlite3
import string
from random import choice
from wsgiref import simple_server
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

app = Flask(__name__)
app.config.from_object(__name__)

def connect_db():
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

def init_db():
    db = connect_db()
    with app.open_resource('db/schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()

    print 'Initialized the Database'

@app.route('/')
def index():
    return render_template('index.html')

def start(host, port, db_path, secret_key = ''.join(choice(string.ascii_letters + string.punctuation + string.digits) for x in range(64))):
    app.config.update(dict(
        DATABASE = db_path,
        SECRET_KEY = secret_key
    ))

    if not os.path.isfile(db_path):
        init_db()

    httpd = simple_server.make_server(host, port, app)
    print 'Server Started at %s:%d\n' % (host, port)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print '\nShutting Down.'
