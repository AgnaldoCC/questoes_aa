n = int(input())
 
for i in range(n):
  mapa = {}
 
  p = input()
  h = input()
 
  for i in range(len(p)):
    if(mapa.get(p[i])):
      mapa[p[i]] += 1
    else:
      mapa[p[i]] = 1
 
  resp = "NO"
 
  for i in range(len(h)-len(p)+1):
    mapa2 = {}
    for j in range(i, i+len(p)):
      if(mapa2.get(h[j])):
        mapa2[h[j]] += 1
      else:
        mapa2[h[j]] = 1
 
    if(mapa == mapa2):
      resp = "YES"
 
  print(resp)