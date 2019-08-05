# поиск подстроки
n = int(input())
I = int(input())  # length of string
d = int(input())  # max number of errors
str1 = input()
k = 0
l = len(str1)
for i in range(l - I):
    read = str1[i:i + I]
    j = 0
    t = 0
    ans = []
    while t != -1:
        t = str1[j:].find(read)
        if t == -1:
            break
        ans.append(t + j)
        j = j + t + 1
    if len(ans) >= n:
        break
print(ans)  # positions of equal substrings