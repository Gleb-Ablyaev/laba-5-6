import matplotlib.pyplot as plt
import time
import numpy as np
try:
    N = int(input("Введите количество строк и столбцов квадратной матрицы больше 3 и меньше 184:"))
    if (N >= 4) and (N <= 183):
        K = int(input("Введите число К:"))
        program = time.time()
        start = time.time()
        A = np.zeros((N, N), dtype=int)
        F = np.zeros((N, N), dtype=int)
        for i in range(N):                                         # Формируем матрицу А
            for j in range(N):
                A[i][j] = np.random.randint(-10, 10)
        middle = time.time()
        print("Матрица A:\n", A, "\nВремя:", middle - start)
        for i in range(N):                                         #формируем матрицу F копируя из матрицы А
            for j in range(N):
                F[i][j] = A[i][j]
        n = N // 2                                                 #размерность подматрицы
        start = time.time()
        B = np.zeros((n, n), dtype=int)                            #формируем матрицу C
        for i in range(n):
            for j in range(n):
                B[i][j] = A[i][j+n]
        middle = time.time()
        print("Матрица B:\n", B, "\nВремя:", middle - start)
        nechet = 0
        summ = 0
        for i in range(n):
            for j in range(n):
                if j % 2 != 0 and B[i][j] < K:                #количество чисел меньших К в нечетных столбцах
                    nechet += 1
                if i % 2 == 0:                    #сумма элементов в четных строках
                    summ += B[i][j]
        print("Количество простых чисел в нечётных столбцах:", nechet, "\nкол во нулей чётных строках:", summ)
        if nechet > summ:
            print("\nМеняем E и C симметрично")
            for i in range(n):                                      #E и C симметрично
                for j in range(n):
                    F[N - i - 1][N - j - 1] = A[i][j]
                    F[i][j] = A[N - i - 1][N - j - 1]
        else:
            print("\nМеняем C и B несимметрично")
            for i in range(n):                                      #E и B несимметрично
                for j in range(n):
                    F[i][j] = A[i][n + j]
                    F[i][j+n] = A[i][j]
        print("Матрица A:\n", A, "\nМатрица F:\n", F)
        print("Определитель матрицы А:", round(np.linalg.det(A)), "\nСумма диагональных элементов матрицы F:", np.trace(F))
        G = np.tril(A, k=0)
        if np.linalg.det(A) == 0 or np.linalg.det(F) == 0:
            print("Нельзя вычислить т.к. матрица A или F вырождена")
        elif np.linalg.det(A) > np.trace(F):
            print("Вычисление выражения: A-1*AT – K * F")
            A = np.dot(np.linalg.inv(A), np.transpose(A)) - np.dot(F, K)        #A-1*AT – K * F
        else:
            print("Вычисление выражения: ((A-1 +G-FТ)*K")
            A = (np.linalg.inv(A) + np.tril(A) - np.transpose(F)) * K     #(A-1 +G-FТ)*K
        print("Результат:")
        for i in A:                                                             #Вывод результата
            for j in i:
                print("%5d" % round(j), end=' ')
            print()
        finish = time.time()
        result = finish - program
        print("Время программы: " + str(result) + " секунды")
    else:
        print("\nВы ввели неверное число")
    fig, ax = plt.subplots()  # matplotlib
    ax.set(xlabel='column number', ylabel='value')
    for i in range(N):
        for j in range(N):
            plt.bar(i, A[i][j])
    plt.show()

    fig, ax = plt.subplots()
    ax.set(xlabel='column number', ylabel='value')
    ax.grid()
    for j in range(N):
        ax.plot([i for i in range(N)], A[j][::])
    plt.show()

    ax = plt.figure().add_subplot(projection='3d')
    ax.set(xlabel='x', ylabel='y', zlabel='z')
    for i in range(N):
        plt.plot([j for j in range(N)], A[i][::], i)
    plt.show()
except ValueError:
    print("\nЭто не число")
