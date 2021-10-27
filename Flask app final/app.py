# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from flask import Flask, render_template, request, Response

from helper import run_model
import pandas as pd
#import json
#from wtforms import TextField, Form

#cluster = pd.read_csv('cluster.csv')

#movies = list(cluster['title'])

app = Flask(__name__)

#class SearchForm(Form):
    #autocomp = TextField('Which Movie did you like?', id='movie_autocomplete')

@app.route('/', methods = ['POST', 'GET'])

#@app.route('/_autocomplete', methods=['GET'])
#def autocomplete():
   # return Response(json.dumps(movies), mimetype='application/json')
   # form = SearchForm(request.form)
   # return render_template("search.html", form=form)


def index():
    
    
    
    
    
    if request.method == 'POST':
        
        
        parameter1 = str(request.form['feature 1'])
        
        #list_features = [parameter1]
        
        
        
        prediction = run_model(parameter1)
        
        
        #print(prediction)
        
        
        
        return render_template('main.html', results = prediction)

    else:
        return render_template('main.html')
    
    
    

if __name__ == '__main__':
    app.run(debug=False, port=5800)