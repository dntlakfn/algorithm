for _ in range(3):
    l = sum(list(map(int, input().split())))
    if l == 4:
        print('E')
    elif l == 0:
        print('D')
    elif l == 3:
        print('A')
    elif l == 2:
        print('B')
    elif l == 1:
        print('C')

