A = int(input())
B = int(input())
C = int(input())
le = [0] * 10
s = str(A*B*C)
for i in s:
    le[int(i)] += 1
print(*le, sep="\n")
    