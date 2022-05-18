import numpy as np
if __name__ == "__main__":
    print("Hola Mundo")

    array = np.array([1.5,2,3,4,5], dtype='float32')

    print(array)

    matriz = np.array([range(i,i+3) for i in [1,4,7]])

    print(matriz)

    zeros_array = np.zeros(10,dtype=float)

    print(zeros_array)

    zeros_matriz = np.zeros((3,3),dtype = int)

    print(zeros_matriz)

    random_matrix = np.random.random((3,3))

    print(random_matrix)

    random_array = np.random.random(5)

    print(random_array)

    random_int_matrix = np.random.randint(0,10,(3,3))

    print(random_int_matrix)

