# t = int(input())
# l = ['*'] * t+1
# for i in range(t, 0, -1):
#     print()


t = int(input())
for i in range(-t+1, t):
    print(' ' * abs(i) + '*' * (t - abs(i)), i)

# 1. 출력 줄을 확인한다.
# 2. 별의 개수를 확인한다.
# 2-1. 반복문의 변수(i)를 조정한다.
# 3. 빈칸을 출력한다.