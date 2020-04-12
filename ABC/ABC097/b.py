x = int(input())
l = [1]
for i in range(2,int(x**0.5)+1):
    num = i**2
    while num <= x:
        l.append(num)
        num *= i
print(max(l))
