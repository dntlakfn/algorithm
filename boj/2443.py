x = int(input())
for i in range(x, 0, -1):
    print(' ' *(x-i) + '*' * (i*2-1))
