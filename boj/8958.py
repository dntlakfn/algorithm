times = int(input())

for _ in range(times):
    a = 0
    wjatn = 1
    l = input()
    for i in l:
        if i == "O":
            a += wjatn
            wjatn += 1
        else: wjatn = 1
    print(a)

        
