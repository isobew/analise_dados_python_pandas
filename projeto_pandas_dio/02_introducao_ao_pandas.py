# -*- coding: utf-8 -*-
"""introducao-ao-pandas.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XXldxJY1tunEDY2QXfo9fpsj4l94fqny

Python para análise de dados(Pandas)
"""

#Importando a biblioteca pandas
import pandas as pd

df = pd.read_csv("/content/drive/MyDrive/datasets/Gapminder.csv",error_bad_lines=False, sep=";")

#Visualizando as 5 primeiras linhas
df.head()

df = df.rename(columns={"country":"Pais", "continent":"Continente", "year":"Ano", "lifeExp":"Expectativa de vida", "pop":"Pop Total", "gdpPercap":"PIB"})

df.head(10)

#Total de linhas e colunas
df.shape

df.columns

df.dtypes

df.tail(15)

df.describe()

#quais continentes tem na base, valores únicos da coluna
df["Continente"].unique()

#valores do continente oceania
Oceania = df.loc[df["Continente"] == "Oceania"]
Oceania.head()

Oceania["Continente"].unique()

df.groupby("Continente")["Pais"].nunique()

df.groupby("Ano")["Expectativa de vida"].mean()

df["PIB"].mean()

df["PIB"].sum()

