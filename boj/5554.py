s = 0
for _ in range(4):
    s += int(input())
m = 0
while s >= 60:
    s -= 60
    m += 1
print(m)
print(s)
# print(s // 60)
# print(s % 60)