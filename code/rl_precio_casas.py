import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import hvplot.pandas

from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.linear_model import LinearRegression



if __name__ == "__main__":
    datos = pd.read_csv('./data/casas.csv')
    
    print(datos.head(5))