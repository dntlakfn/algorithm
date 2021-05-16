max_num = 0
lo = 0

for i in range(1, 10):
    num = int(input())
    if max_num < num:
        max_num = num
        lo = i
print(max_num)
print
