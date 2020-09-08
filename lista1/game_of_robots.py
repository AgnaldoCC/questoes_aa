linha1 = input().split()
n = int(linha1[0])
k = int(linha1[1])

ids = input().split()

result = []

cont = 0

for i in range(1, n + 1):
  cont += i
  if cont >= k:
    cont -= i
    print(ids[k - cont - 1])
    break