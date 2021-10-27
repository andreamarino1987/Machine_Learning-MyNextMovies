# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 12:53:02 2021

@author: andre
"""

import pandas as pd
import numpy as np

from sklearn import cluster, datasets
from sklearn.decomposition import PCA
import pickle

cluster = pd.read_csv('cluster.csv')