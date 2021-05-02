a = input().split()
l = '112228'
result = []
for i in range(len(a)):
    result.append(int(l[i]) - int(a[i]))
print(*result)

        