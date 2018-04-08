# -*- coding: utf-8 -*-
"""
@author: Ravikiran
"""

import sys, os
import pandas as pd
import numpy as np


df = pd.DataFrame({'X': [7, 2, 0, 3, 4, 2, 5, 0, 3, 4]})

df = df.assign (Y = df.loc[df.X == 0])

nulval = df['Y'].isnull()

print (nulval,df)

# Need help here: Unable to populate the Y column 


# 2) Create a DatetimeIndex that contains each business day of 2015 and use it to index a Series of random numbers.

date_range_2015 = pd.date_range('1/1/2015', '12/31/2015', freq='B')
series_randn_dtrng_index = pd.Series(np.random.randn(date_range_2015.size), index=date_range_2015)
print("Random numbers with date range as index :\n\n", series_randn_dtrng_index, "\n")


#3) Find the sum of the values in s for every Wednesday

Wed = series_randn_dtrng_index.loc[series_randn_dtrng_index.index.weekday==2]
print("All Wednesday is:", Wed, "\n")

SumWed = series_randn_dtrng_index.loc[series_randn_dtrng_index.index.weekday==2].sum()
print("Sum is:", SumWed, "\n")

#4) Average For each calendar month

AvgForEachMonth= series_randn_dtrng_index.resample('M').mean()

print("Average For each calendar month::: :\n\n", AvgForEachMonth, "\n")


#5) For each group of four consecutive calendar months in s, find the date on which the highest value occurred.

max_idx = series_randn_dtrng_index.resample('4M', closed='left').agg({np.argmax})
print ("For each group of four consecutive calendar months in s, find the date on which the highest value occurred::\n",max_idx.values[0], max_idx.values[1], max_idx.values[2], max_idx.values[3])


