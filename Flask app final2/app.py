# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 18:17:41 2021

@author: andre
"""

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')

def my_function():
    return 'welcome to my page'

if __name__ == '__main__':
    app.run(debug=(False), port = 3500)