# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 12:34:02 2021

@author: andre
"""

import pandas as pd
movies = pd.read_csv('movies.csv')
ratings = pd.read_csv('ratings.csv')
ratings = ratings.drop('timestamp', axis=1)
links = pd.read_csv('links.csv')
tags = pd.read_csv('tags.csv')
tags = tags.drop('timestamp', axis=1)
genome_tags =pd.read_csv('genome-tags.csv')
genome_scores = pd.read_csv('genome-scores.csv')
df = pd.merge(movies, ratings, on = 'movieId', how = 'outer')
df2 = pd.merge(df, tags, on = 'movieId', how = 'outer')
df2