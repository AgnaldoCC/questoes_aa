def isVowel(letter):
    return letter in ['a','e','i','o','u']

def isEven(digit):
    return digit in ['0','2','4','6','8']

word = input()
cont = 0
for i in word:
    if(i.isalpha() and isVowel(i)):
        cont += 1
    if(i.isdigit() and not isEven(i)):
        cont += 1
print(cont)