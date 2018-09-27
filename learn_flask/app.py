# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 11:25:21 2018

@author: zouco
"""

from flask import Flask
from flask import request
from flask import render_template

from SPIDER_crawler import ThomasnetCrawler

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html") # this should be the name of your html file

@app.route('/', methods=['POST'])
def my_form_post():
    text1 = request.form['text1']
    text = str(text1)
    
    tc = ThomasnetCrawler()
    df = tc.run(text, number_suppliers=2)
    
    html = "<ul>"
    for i in df.name:
       html += "<li>{}</li>".format(i)
    html += "</ul>"
    
    
    print(text.upper())
    
    return html


if __name__ == '__main__':
    app.run()


