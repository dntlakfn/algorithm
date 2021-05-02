x = int(input())
for i in range(-(x-1), x):
    print(' '*(x-abs(i)-1) + '*' * (abs(i)*2 + 1))