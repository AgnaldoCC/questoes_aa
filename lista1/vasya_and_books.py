def solution(books, step):
    mapa = {}

    for i in books:
        mapa[i] = 1
    
    result = ['0' for i in range(len(books))]
    i, j = 0, 0
    current_steps = 0

    while j < len(step):
        current_steps += 1
        if step[j] not in mapa or books[i] not in mapa:
            result[j] = '0'
            j += 1
            current_steps = 0
        elif step[j] == books[i]:
            result[j] = str(current_steps)
            j += 1
            i += 1
            current_steps = 0
        else:
            del mapa[books[i]]
            i += 1
 
    return ' '.join(result)


book = int(input())
books = list(map(int, input().split()))
steps = list(map(int, input().split()))

print(solution(books, steps))