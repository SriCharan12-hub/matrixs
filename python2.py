a=int(input())
b=int(input())
d=[]
f=[]
g=[]
for i in range(a):
    c=list(map(int,input().split()))
    d+=[max(c)]
    f+=[min(c)]
    g+=[sum(c)]
    
print(d)
print(f)
print(g)

    
    