n = int(input())

for i in range(n):
    word = input()
    if(len(word) == 1):
        print(word)
    else:
        mapa = {}
        for i in range(len(word)-1):
            if(word[i] == word[i+1]):
                if(word[i] not in mapa.keys()):
                    mapa[word[i]] = 1
                else:
                    mapa[word[i]] += 1
        result = []
        for i in set(word):
            if(i not in mapa.keys()):
                result.append(i)
            else:
                if(word.count(i) != mapa[i] + 1):
                    result.append(i)
        print(''.join(sorted(result)))