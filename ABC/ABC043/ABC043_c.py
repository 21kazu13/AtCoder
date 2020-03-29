n = int(input())
A = list(map(int, input().split()))
mini = 40000*100
for n in range(-100,101):
    cost = 0
    for item in A:
        cost += (item-n)**2
    if cost < mini:
        mini = cost
print(mini)