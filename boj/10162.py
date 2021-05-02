T = int(input())
A = 300
B = 60
C = 10

a = T // A
T = T % A
b = T // B
T = T % B
c = T // C
T = T%C
if T != 0:
    print(-1)
else:
    print(a, b, c)