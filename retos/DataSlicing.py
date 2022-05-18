import numpy as np

np.random.seed(0)

random_data = np.random.randint(10,size=(10,10))

#Obtener los elementos de las filas 4-7 y Columnas 2-8
print(random_data[4:7,2:8])

#Obtener los elementos de las filas 0-5 y columnas 0-3
print(random_data[:5,:3])

#Obtener los elementos de las últimas 3 filas y últimas 5 columnas
print(random_data[-3:,-5:])

##Al usar copy se copian los datos
copia_data = random_data[-3:,-5:].copy()

print()

#Al no usar copy, se le da una vista a la variable, es decir las filas de las matriz original pueden ser modificadas desde la vista
nocopy = random_data[-3:,-5:]