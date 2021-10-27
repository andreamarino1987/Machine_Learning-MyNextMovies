# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 14:23:04 2021

@author: andre
"""
import pandas as pd

cluster = pd.read_csv('cluster.csv')

cluster_kmode = pd.read_csv('cluster_kmode.csv')

#movies = input('choose a movie:')


def run_model(movies):
    final = cluster_kmode[cluster_kmode['clusters'] == list(cluster_kmode[cluster_kmode['title'] == movies]['clusters'])[0]].sort_values(by = 'rating' , ascending = False).head()['title'].values 
    if movies in final:
        total_list = cluster_kmode[cluster_kmode['clusters'] == list(cluster_kmode[cluster_kmode['title'] == movies]['clusters'])[0]].sort_values(by = 'rating' , ascending = False)['title'].values 
        
        extra_movie = total_list[5]
        #print(extra_movie)
        new_final = list(final)
        #print(new_final)
        new_final.append(extra_movie)
        new_final.remove(movies)
        return new_final
    
    return final
    



    
#print(run_model('Near Dark (1987)'))