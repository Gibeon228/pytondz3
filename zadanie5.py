# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
def Niga_fibonachi(n):
    if (n<-2):
        return Niga_fibonachi(n+2) - Niga_fibonachi(n+1)
    
    if (n == -2):
        return -1

    if (n == -1):
        return 1
    if (n == 0):
        return 0
    if (n == 1):
        return 1
    if (n>1):
        return Niga_fibonachi(n-2) + Niga_fibonachi(n-1)

print ("Введите число n")
n = int(input())
for i in range (-1*n, n+1):
    print(Niga_fibonachi(i))
