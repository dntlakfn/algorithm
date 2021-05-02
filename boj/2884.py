H, M = map(int, input().split())
if M >= 45:
    print(H, M-45)
else:
    a = 45
    a = abs(M-a)
    M = 60
    if H == 0:
        H = 24
    H = H - 1
    M = M - a
    print(H, M)
    
    
