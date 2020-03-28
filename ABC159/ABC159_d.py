n = int(input())
A = list(map(int,input().split()))

number = [0]*n
for item in A:#O(n)
    number[item-1] += 1

ans = 0

for items in number:
    ans += items*(items-1)//2

for item in A:
    print(ans - (number[item-1]-1))