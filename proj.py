#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 13:57:35 2019

@author: dewaniadi
"""
import pandas as pd
import xgboost as xgb
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from IPython.display import display

data=pd.read_csv("final_dataset.csv")
display(data.head())


#calculating win rate for home teams
n_matches = data.shape[0]
n_features = data.shape[1] - 1
n_homewins = len(data[data.FTR == 'H'])
win_rate = (float(n_homewins) / (n_matches)) * 100


print ("Total number of matches: {}".format(n_matches))
print ("Number of features: {}".format(n_features))
print ("Number of matches won by home team: {}".format(n_homewins))
print ("Win rate of home team: {:.2f}%".format(win_rate))