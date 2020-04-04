s = int(input())

def f(n):
    if n%2 == 0:
        return n//2
    else:
        return n*3+1

A = [s]
ans = 1

while True:
    ans += 1
    num = f(A[-1])
    if num in A:
        print(ans)
        break
    else:
        A.append(num)
