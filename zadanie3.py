# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением 
# дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
# по идее минимальное значение дробной части у 5 (элемент с индексом 3) и равна она 0, но да ладно


def Magic (list2):
    str1 = str(list2[0]).split(".")
    max = float (str1[1])
    min = float (str1[1])    
    help = 0
    flag = 0
    for i in range (1, len(list2)):
        if (type (list2[i]) == float):
            str1 = str(list2[i]).split(".")
            while (str1[1][help] == "0"):
                help+=1
                flag = 1
            if (max < (float (str1[1])) / (10 ** (help+1))):
                max = (float (str1[1])) / (10 ** (help+1))
            if (min > (float (str1[1])) / (10 ** (help+1))):
                min = (float (str1[1])) / (10 ** (help+1))
            help = 0
            max = max
            print(max, min)
    while (min > 1):
        min = min /10
        max = max / 10
    while (max > 1):
        max = max / 10
    return round ((max-min), 5)
            
list1 = [1.1, 1.456, 3.345, 5, 10.01]
result = Magic(list1)
print (result)