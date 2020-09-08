import math
def isPrime(num):
    if(num < 2):
        return True
    if(num % 2 == 0 or num % 3 == 0):
        return False
    for i in range(2, int(math.sqrt(num))):
        if (num % i) == 0:        
            return False
    return True

n = int(input())
cont = 1
while(True):    
    if(isPrime(n * cont + 1)):
        cont += 1
    else:
        print(cont)
        break
