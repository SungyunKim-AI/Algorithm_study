import numpy as np
import pandas as pd

path = "C:/Users/user/Desktop/iris.csv"
dataset = pd.read_csv(path)
mColumns = list(dataset.columns)

petal_data = dataset['petal_length'] >= 1.5
petal = dataset.copy()[petal_data]

diff = petal['sepal_length'] - petal['petal_length']
petal['diff'] = diff

print(petal.head(6))