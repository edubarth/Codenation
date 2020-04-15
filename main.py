#!/usr/bin/env python
# coding: utf-8

# # Desafio 1
# 
# Para esse desafio, vamos trabalhar com o data set [Black Friday](https://www.kaggle.com/mehdidag/black-friday), que reúne dados sobre transações de compras em uma loja de varejo.
# 
# Vamos utilizá-lo para praticar a exploração de data sets utilizando pandas. Você pode fazer toda análise neste mesmo notebook, mas as resposta devem estar nos locais indicados.
# 
# > Obs.: Por favor, não modifique o nome das funções de resposta.

# ## _Set up_ da análise

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


black_friday = pd.read_csv("black_friday.csv")


# ## Inicie sua análise a partir daqui

# In[4]:


print(black_friday.head())


# In[5]:


print(black_friday.info())


# In[6]:


print(black_friday.shape)


# ## Questão 1
# 
# Quantas observações e quantas colunas há no dataset? Responda no formato de uma tuple `(n_observacoes, n_colunas)`.

# In[10]:


def q1():
    return black_friday.shape
    


# ## Questão 2
# 
# Há quantas mulheres com idade entre 26 e 35 anos no dataset? Responda como um único escalar.

# In[11]:


print(len(black_friday.query('Age == \"26-35\" & Gender == \"F\"')))


# In[5]:


def q2():
    return len(black_friday.query('Age == \"26-35\" & Gender == \"F\"'))


# ## Questão 3
# 
# Quantos usuários únicos há no dataset? Responda como um único escalar.

# In[69]:


print(black_friday['User_ID'].nunique())


# In[6]:


def q3():
    return black_friday['User_ID'].nunique()


# ## Questão 4
# 
# Quantos tipos de dados diferentes existem no dataset? Responda como um único escalar.

# In[16]:


print(len(black_friday.dtypes.value_counts()))


# In[7]:


def q4():
    return len(black_friday.dtypes.value_counts())


# ## Questão 5
# 
# Qual porcentagem dos registros possui ao menos um valor null (`None`, `ǸaN` etc)? Responda como um único escalar entre 0 e 1.

# In[26]:


print(black_friday.shape[0])


# In[36]:


nulos =  black_friday.isnull().sum().max()


# In[37]:


print(nulos)


# In[38]:


print(nulos / black_friday.shape[0])


# In[8]:


def q5():
    return (nulos / black_friday.shape[0])


# ## Questão 6
# 
# Quantos valores null existem na variável (coluna) com o maior número de null? Responda como um único escalar.

# In[9]:


def q6():
    return (black_friday.isnull().sum().max())


# ## Questão 7
# 
# Qual o valor mais frequente (sem contar nulls) em `Product_Category_3`? Responda como um único escalar.

# In[47]:


print(black_friday['Product_Category_3'].describe())


# In[48]:


print(int(black_friday['Product_Category_3'].mode()))


# In[10]:


def q7():
    return (int(black_friday['Product_Category_3'].mode()))


# ## Questão 8
# 
# Qual a nova média da variável (coluna) `Purchase` após sua normalização? Responda como um único escalar.

# In[50]:


normalizar=black_friday[['Purchase']]
print(normalizar)


# In[55]:


normalizado=(normalizar-normalizar.min())/(normalizar.max()-normalizar.min())
print(normalizado)


# In[57]:


print(float(normalizado.mean()))


# In[52]:


def q8():
    return (float(normalizado.mean()))


# ## Questão 9
# 
# Quantas ocorrências entre -1 e 1 inclusive existem da variáel `Purchase` após sua padronização? Responda como um único escalar.

# In[67]:


padronizado=(normalizar-normalizar.mean())/normalizar.std()
print(padronizado)


# In[62]:


print(len(padronizado.query('Purchase >= -1 & Purchase <= 1')))


# In[12]:


def q9():
    return (len(padronizado.query('Purchase >= -1 & Purchase <= 1')))


# ## Questão 10
# 
# Podemos afirmar que se uma observação é null em `Product_Category_2` ela também o é em `Product_Category_3`? Responda com um bool (`True`, `False`).

# In[65]:


print(black_friday.isna().query('Product_Category_2 == True & Product_Category_3 == False'))


# In[66]:


print(len(black_friday.isna().query('Product_Category_2 == True & Product_Category_3 == False')) == False)


# In[13]:


def q10():
    return (len(black_friday.isna().query('Product_Category_2 == True & Product_Category_3 == False')) == False)

