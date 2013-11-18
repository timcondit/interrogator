import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
        abort, render_template, flash

# configuration
DATABASE = r'C:\Source\accurev_txn_report\accurev_txn_report\flaskr.db'
DEBUG = True
SECRET_KEY = 'chachonga'
USERNAME = 'admin'
PASSWORD = 'admin'

app = Flask(__name__)
app.config.from_object(__name__)


def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

if __name__ == '__main__':
    app.run()
