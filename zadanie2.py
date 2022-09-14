# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

def Mult(list3):
    finish_list3 = []
    mult = 1
    if (len(list3) % 2 == 1):
        long = int(len (list3)/2+1)
    else:
        long = int(len (list3)/2)
    for i in range (long):
        mult = list3[i] * list3[len(list3)-i-1]
        finish_list3.append(mult)
    return finish_list3


list1 = [2, 3, 4, 5, 6]
list2 = [2, 3, 5, 6]
finish_list1 = Mult(list1)
finish_list2 = Mult(list2)
print(finish_list1)
print(finish_list2)
