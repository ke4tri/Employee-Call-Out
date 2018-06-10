'''
This was used to clean the original .csv data file so something more useable. 

'''

import numpy as np
import pandas as pd
from datetime import datetime as dt
import matplotlib.pyplot as plt
import csv
import matplotlib.ticker as ticker
import matplotlib

df = pd.read_csv('new2_022518.csv', header=None)

df = df.drop([0,241])

del df[9]
del df[0]
del df[6]
del df[2]
del df[4]
del df[7]
del df[5]


df = df.rename(columns=({1:'Name', 3:'Address', 8:'City',10:'Old Start', 11:'New Start'}))

df.to_csv('022518_clean.csv')

