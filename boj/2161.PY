from collections import deque
N = int(input())
queue = deque(list(range(1, N+1)))
result = []
t = True
while len(queue) != 1:
    x = queue.popleft()
    if t:
        result.append(x)
        t = not t
    else: 
        queue.append(x)
        t = not t
result.append(queue[0])
print(*result)



