casos = int(input())
for i in range(casos):
    entrada = input().split()
    a = int(entrada[0])
    b = int(entrada[1])
    n = int(entrada[2])
    menor = a
    maior = b
    if(a > b):
        menor = b
        maior = a
    response = []
    response.append(menor)
    response.append(maior)
    while(response[-1] <= n):
        response.append(response[-1] + response[-2])
    print(len(response) - 2)