import sys
input = sys.stdin.readline

testCase = int(input())
for i in range(testCase):
    a, d = map(int, input().split())
    print(a+d)
