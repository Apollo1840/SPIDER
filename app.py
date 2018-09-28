# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 11:25:21 2018

@author: zouco
"""

from flask import Flask
from flask import render_template
from flask import request
import time

from SPIDER_crawler import ThomasnetCrawler


app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def my_form_post():
    print('fuck')
    text1 = request.form['mname']
    print(text1.upper())
    return render_template("index.html")
    
 
@app.route('/materials')
def api_hello():
    if 'name' in request.args:

    	 #with open('file.txt', 'w') as f:
    	 #f.write(str.upper(request.args['name']) + '\n')
        print('scraping...')
        tc = ThomasnetCrawler()
        tc.run(request.args['name'], number_suppliers=3)
        print('finished.')
        return 'success'
    else:
        return 'Invalid arguments'
   
if __name__ == '__main__':
    app.run()
    