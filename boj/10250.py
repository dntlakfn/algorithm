for _ in range(int(input())):
    h, w, n = map(int, input().split())
    H = 0
    O = 0
    x = n % h
    if x == 0: H = h
    else: H = x

    y = n // h
    if H == h: O = y
    else: O = y+1

    H = str(H)
    O = "0"+str(O) if len(str(O)) == 1 else str(O)
    print(H + O)