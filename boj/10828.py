f = int(input())
l = []
for i in range(f):
    x = input().split()
    if x[0] == 'push':
        l.append(x[1])
    elif x[0] == 'pop':
        if len(l) == 0:
            print(-1)
        else: print(l.pop())
    elif x[0] == 'size':
        print(len(l))
    elif x[0] == 'empty':
        if len(l) == 0:
            print(1)
        else: print(0)
    elif x[0] == 'top':
        if len(l) == 0:
            print(-1)
        else: print(l[-1])




