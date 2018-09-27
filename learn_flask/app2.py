# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 11:25:21 2018

@author: zouco
"""

from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/')
def json():
    return render_template('json.html')

@app.route('/background_process_test')
def background_process_test():
    print("Hello")
    return "nothing"

if __name__ == '__main__':
    app.run()