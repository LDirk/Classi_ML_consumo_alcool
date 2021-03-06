# -*- coding: utf-8 -*-
"""NAIVE_BAYES_Gaussian_MAX.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1a1FTBLbkmgYIUVERLG4Yf2CqtDxZJV56
"""

import pandas as pd


from sklearn.naive_bayes import BernoulliNB
from sklearn.model_selection import train_test_split

dados = pd.read_csv("Testes_ML_classi.csv")

X = dados[["Sexo","Solitude","Fumou","Pais_Fumante","amigod_drogados","idade"]]
Y = dados[["Ja_bebeu"]]

from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split 
from sklearn.metrics import accuracy_score
import numpy as np

SEED = 5
np.random.seed(SEED)
treino_x, teste_x, treino_y, teste_y = train_test_split(x, y, test_size = 0.25, stratify = y)

print("Treinaremos com %d elementos e testaremos com %d elementos" % (len(treino_x), len(teste_x)))

modelo = GaussianNB()
modelo.fit(treino_x, treino_y)
previsoes = modelo.predict(teste_x)

acuracia = accuracy_score(teste_y, previsoes)*100
print("A acurácia foi %.2f%%" % acuracia)

i = 0.10 #test size 

vetor_test = []
acu =[] #acuracias 


while i<1: 

  SEED = 5
  np.random.seed(SEED)
  treino_x, teste_x, treino_y, teste_y = train_test_split(x, y, test_size = i , stratify = y)
  modelo = GaussianNB()
  modelo.fit(treino_x, treino_y)
  previsoes = modelo.predict(teste_x)
  acuracia = accuracy_score(teste_y, previsoes) * 100

  acu.append(acuracia)
  vetor_test.append(i)
  i = i + 0.01
  print(i)

acu

n_max = (max(acu)) # Melhor valor para acuracia entre um intervalo de test_size de 0.10 até 0.99
n_pos = acu.index(n_max) # Posição do melhor valor

print(max(acu)) # valor da maior acuracia
print(n_pos) # Posição da maior acuracia

vetor_test[11] # valor do test que maximiza a acuracia do SVM, TEST_SIZE = 0.21

acu

n_max = (max(acu)) # Melhor valor para acuracia entre um intervalo de test_size de 0.10 até 0.99
n_pos = acu.index(n_max) # Posição do melhor valor

print(max(acu)) # valor da maior acuracia
print(n_pos) # Posição da maior acuracia

vetor_test[0] # valor do test que maximiza a acuracia do SVM, TEST_SIZE = 0.10