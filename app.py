from queue import Empty
import re, logging
from flask import Flask, render_template, redirect, request, session
from flask.templating import render_template
import random
import sqlite3
 
app = Flask(__name__)
app.secret_key = "KAI"  #loging



@app.route('/')
def top():
    return render_template('index.html')


#@app.route('/')
#def top():
#    return render_template('index.html')

@app.route('/GOAT_Dance')
def GOAT():
    return render_template('MV_times_GOAT_Dance.html')

if __name__ == "__main__":
    app.run()
