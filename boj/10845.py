from collections import deque
import sys
input = sys.stdin.readline
queue = deque([])
f = int(input())
for i in range(f):
    l = len(queue)
    x = input().split()
    if x[0] == 'push': queue.append(x[1])
    elif x[0] == 'pop': print(-1 if l == 0 else queue.popleft())
    elif x[0] == 'size': print(l)
    elif x[0] == 'empty': print(1 if l == 0 else 0)
    elif x[0] == 'front': print(-1 if l == 0 else queue[0])
    elif x[0] == 'back': print(-1 if l == 0 else queue[-1])