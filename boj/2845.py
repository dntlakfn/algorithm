a,b = map(int, input().split())
l = list(map(int, input().split()))
s = a*b
for i in range(len(l)):
    l[i] -= s
print(" ".join(map(str, l)))