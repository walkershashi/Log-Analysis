#!/usr/bin/env python3

import sys
import pandas as pd

#creating a list containing all the csv files passed
files = sys.argv[1:]

for file in files:
    name = file.split('_')[0]
    file = pd.read_csv(file) #converting the file into dataframe
    html_file = file.to_html("{}_Stats.html".format(name)) # converting to html file
