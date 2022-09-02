n=int(input())
a=[int(input()) for i in range(n)]
d={}
for i in a:
 if i not in d:
  d[i]=1
 else:
  d[i]+=1
v=list(d.values())
k=list(d.keys())
for i in range(len(v)):
 if v[i]>1:
  print(k[i])
  break
 else:
  print(-1)
  break