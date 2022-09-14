# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def Dva (b):
    list1 = []
    while (b>1):
        list1.append(b%2)
        b= int (b/2)
        
    list1.append(1)
    print (list1)
    for i in range (len(list1)):
        print (list1[(len(list1)) - i-1])


print("Введите число")
a = int (input())
Dva(a)