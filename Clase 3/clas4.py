# %%
import numpy as np

# %%
np.random.seed(0) #Siempre Obtiene los mismos numeros aleatorios

x1 = np. random.randint(10,size = 10)

x2 = np.random.randint(10,size = (3,3))

x3 = np.random.randint(10,size=(3,4,5))

# %%
print(x1)

# %%
print(x2)
print(x3)

# %%
numeros = np.array([1,2,3,4,5])

# Indexación
numeros[1]

# %%
#Array Slicing

# %%
# x[start:stop:step]

x = np.arange(10)

# %%
x

# %%
#Obtiene los elementos desde la posición 0 hasta la 5
x[0:5]

# %%
#Obtiene los primeros 5 elementos
x[:5]

# %%
#Obtiene los elementos desde la posición 5
x[5:]

# %%
#Obtiene los elementos de la posición 2 a la 7

x[2:7]

# %%
#Obtiene los elementos de la posición 2 a la 7, de 2 en 2

x[2:7:2]

# %%
# Revertir el arreglo

x[::-1]

# %%
pares = x[2:7:2]

pares [::-1]

# %%
x[7:2:-1]

# %%
data = np.array([np.arange(i*5,i*5+5) for i in range(5)])

# %% [markdown]
# Slicing en arreglos multidimensionales

# %%
data

# %%
# x[row][column]
data[2][1]

# %%
#Obtener las primeras dos filas y 3 columnas
data[:2,:3]

# %%
np.random.seed(0)
random_data = np.random.randint(10,size=(10,10))

random_data

# %%
#Obtener los elementos de las filas 4-7 y Columnas 2-8

#Obtener los elementos de las filas 0-5 y columnas 0-3

#Obtener los elementos de las últimas 3 filas y últimas 5 columnas

# %%



