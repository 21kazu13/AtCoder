s = input()
se = (s)
k = int(input())
n = len(s)

se = set()
for i in range(n):
    for j in range(i+1,i+1+k):
#        print(i,j,s[i:j])
        se.add(s[i:j])
#print(se)
l = sorted(list(se))
print(l[k-1])
        










#TLE 
'''
se = set()
for i in range(n):
    for j in range(i+1,n+1):
#        print(i,j,s[i:j])
        se.add(s[i:j])
#print(se)
l = sorted(list(se))
print(l[k-1])
'''