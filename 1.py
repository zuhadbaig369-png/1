import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = pd.read_csv("Titanic Dataset.csv")
data.head(5)
data.dtypes
data.isnull().sum()
data.describe()
print(data.info)