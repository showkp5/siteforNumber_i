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

@app.route('/BYC')
def BYC():
    return render_template('MV_times_BYC.html')

@app.route('/BYC_Dance')
def BYC_Dance():
    return render_template('MV_times_BYC_Dance.html')

@app.route('/BON')
def BON():
    return render_template('MV_times_BON.html')

@app.route('/BON_Dance')
def BON_Dance():
    return render_template('MV_times_BON_Dance.html')

@app.route('/INZM')
def INZM():
    return render_template('MV_times_INZM.html')

@app.route('/INZM_HBL')
def INZM_HBL():
    return render_template('MV_times_INZM_HBL.html')

@app.route('/ALL')
def ALL():
    return render_template('MV_times_ALL.html')

@app.route('/ALLFromRelease')
def ALLFromRelease():
    return render_template('MV_times_ALLFromRelease.html')

@app.route('/HRKGM')
def HRKGM():
    return render_template('MV_times_HRKGM_OV.html')

@app.route('/GOD_i')
def GOD_i():
    return render_template('MV_times_GOD_i.html')

@app.route('/GOAT_Choreo')
def GOAT_Choreo():
    return render_template('MV_times_GOAT_Choreo.html')

@app.route('/UMA')
def UMA():
    return render_template('MV_times_UMA.html')

@app.route('/UrZone')
def UrZone():
    return render_template('MV_times_UrZone.html')

@app.route('/GBAD_Remix')
def GBAD_Remix():
    return render_template('MV_times_GBAD_Remix.html')

@app.route('/ATAMI')
def ATAMI():
    return render_template('MV_times_ATAMI.html')

#@app.route('/Ways')
#def Ways():
#    return render_template('MV_times_100Ways.html')

if __name__ == "__main__":
    app.run()
