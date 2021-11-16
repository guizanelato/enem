
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mt
mt.use('TkAgg')
import seaborn as sns
import numpy as np
from scipy.stats import norm
from sklearn.preprocessing import StandardScaler
from scipy import stats
import warnings

FILE = "dados/base_teste/train_test.csv"

headers = []

#1: Carrega a base de dados
dados = pd.read_csv(FILE).dropna()
var_dependente = dados['NU_NOTA_MT']

print(var_dependente.head())

def teste(a):
    return 0 if a == 'M' else 1


#print(stats.pearsonr(var_dependente, sexo))


#3: Analisar a nota de matemática

print(var_dependente.describe())

#sns.distplot(var_dependente)
#plt.show()

print("Skewness: %f" % var_dependente.skew())
print("Kurtosis: %f" % var_dependente.kurt())

#4: Relacionamentos 

label = "Q002"
dados = pd.concat([var_dependente, dados['Q002']], axis=1)
dados.plot.scatter(x=label, y='NU_NOTA_MT', ylim=(0.80))
plt.show()



