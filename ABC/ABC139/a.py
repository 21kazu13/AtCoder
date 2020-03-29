s = input()
t = input()
a = list(zip(s,t))
ans = 0
for item in a:
    if item[0] == item[1]:
        ans += 1


print(ans)