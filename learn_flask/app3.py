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
def home():
    return render_template("home2.html") # this should be the name of your html file

@app.route('/', methods=['POST'])
def my_form_post():
    text1 = request.form['text1']
    print(text1.upper())
    return "The suppliers are : ...."

if __name__ == '__main__':
    app.run()