N = int(input())
l = []
for i in range(1, N+1):
    student = list(map(int, input().split()))
    student.append(i)
    l.append(student)
l.sort(reverse=True)
max_score = l[0][0]
same_score_List = [l[0]]
for i in range(1, N):
    if l[i][0] < max_score:
       break
    same_score_List.append(l[i])
same_score_List.sort(key=lambda x: x[1])
min_repeat = same_score_List[0][1]
same_repeat_List = [same_score_List[0]]
for i in range(1, len(same_score_List)):
    if min_repeat > same_score_List[i][1]: break
    same_repeat_List.append(same_score_List[i])

same_repeat_List.sort(key=lambda x: x[2])
print(same_repeat_List[0][3])