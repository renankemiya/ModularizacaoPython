import pandas as pd
from preprocessing.normalize import *

iris_dataset = pd.read_csv("./data/iris.csv")

normalized_data = normalize(iris_dataset[["sepal.length", "sepal.width", "petal.length", "petal.width"]])

print(normalized_data.head(5))
print('---------------------')
print(iris_dataset.head(5))
