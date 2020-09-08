x = int(input())
find = False
for a in range(1,x+1):
    for b in range(1, x+1):
        if(a % b == 0 and a * b > x and a / b < x):
            print(a, b)
            find = True
            break
    if(find):
        break
if(not find):
    print(-1)