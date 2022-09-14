
def Niga_fibonachi(n):

    if (n<-2):
        return Niga_fibonachi(n+2) - Niga_fibonachi(n+1)
    
    if (n == -2):
        return -1

    if (n == -1):
        return 1

print ("Введите число n")
n = int(input())
print(Niga_fibonachi(n))