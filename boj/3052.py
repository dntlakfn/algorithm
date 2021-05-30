count = 0
l = []
for _ in range(10):
    a = int(input()) % 42
    if a in l:
        continue
    else: 
        l.append(a)
        count += 1
print(count)


