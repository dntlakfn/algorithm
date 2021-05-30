import sys
input = sys.stdin.readline
N = int(input())
score = 1
highest = 0
L = []
for i in range(N):
    x = int(input())
    L.append(x)
L.reverse()
highest = L[0]
for i in range(1, N):
    if highest < L[i]:
        highest = L[i]
        score += 1
print(score)