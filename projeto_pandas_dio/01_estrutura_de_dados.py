# -*- coding: utf-8 -*-
"""Estrutura_de_dados.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_3JrZKFv-Bd0t4_LHMB2blGe9xEvFh23

Análise de dados com Python e Pandas - Estrutura de dados

**Listas**
"""

#Criando uma lista chamada "animais"
animais = [1,2,3]
animais

animais = ["cachorro", "gato", 123456, 6.5]
animais

#Imprimindo o primeiro elemento da lista
animais[0]

#Imprimindo o 4 elemento da lista
animais[3]

#Substituindo o primeiro elemeento da lista
animais[0] = "papagaio"

animais

#Removendo gato da lista
animais.remove("gato")

animais

len(animais)

"gato" in animais

lista = [500, 30, 300, 80, 10]

max(lista)

min(lista)

animais.append("leao")

animais

animais.extend(["cobra", 6])

animais.count("cachorro")

animais

lista.sort()

lista

"""----------

**Tuplas**
"""

#As tuplas usam parêntesis como sintaxe
tp = ("Banana", "Maçã", 10, 50)

#Retornando o primeiro elemento
tp[0]

#Diferente das listas as tuplas são imutáveis, o que quer dizer que não podemos alterar os seus elementos
tp[0] = "Laranja"

tp.count("Maçã")

tp[0:2]

"""---------

**Dicionários**
"""

#Para criar um dicionário utilizamos as {}
dc = {"Maçã":20, "Banana":10, "Laranja":15, "Uva":5} #Dicionários trabalham com o conceito de chave e valor

dc

#Acessando o valor de um dicionário através da chave
dc["Maçã"]

#Atualizando o valor da Maçã
dc["Maçã"] = 25
dc

#Retornando todas as chaves do dicionário
dc.keys()

#Retornando os valores do dicionário
dc.values()

#Verificando se já existe uma chave no dicionário e caso não exista, inserir
dc.setdefault("Limão", 22)

dc