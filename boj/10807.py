input()
count = 0
n = map(int, input().split())
v = int(input())
for i in n:
    if i == v:
        count += 1
print(count)