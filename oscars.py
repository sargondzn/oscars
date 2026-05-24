import pandas as pd
import numpy as np
import os 

df = pd.read_csv('oscars.csv', sep=None, engine='python')

df.head()