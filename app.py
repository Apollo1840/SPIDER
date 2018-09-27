# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 11:25:21 2018

@author: zouco
"""

from flask import Flask
from flask import render_template
from flask import request
import time

app = Flask(__name__)

from SPIDER_crawler import ThomasnetCrawler

@app.route('/')
def my_form():
    return render_template("index.html")

 
@app.route('/materials')
def api_hello():
    if 'name' in request.args:
    	 #with open('file.txt', 'w') as f:
    	 #f.write(str.upper(request.args['name']) + '\n')
        print('scraping...')
        tc = ThomasnetCrawler()
        tc.run(request.args['name'], number_suppliers=3)
        return 'success'
    else:
        return 'Invalid arguments'
   
if __name__ == '__main__':
    app.run()