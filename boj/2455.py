max_p = 0
people = 0
for _ in range(4):
    a, o = map(int, input().split())
    people = (o-a) + people
    max_p = max(max_p, people)
print(max_p)