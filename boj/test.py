x = int(input())
for i in range(-(x-1), x):
    print(' ' * (abs(i)) + '*' * ((x-abs(i))*2-1))