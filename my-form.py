# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 11:25:21 2018

@author: zouco
"""

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def my_form():
    return 'Fuck'
    # return render_template("index.html") # this should be the name of your html file

if __name__ == '__main__':
    app.run()