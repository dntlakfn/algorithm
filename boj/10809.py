l = [-1]*26
s = input()
for i in range(len(s)):
    d = ord(s[i]) - ord('a')
    if l[d] == -1:
        l[d] = i
print(l)