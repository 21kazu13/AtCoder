k, n = map(int,input().split())
A = list(map(int,input().split()))
mdist = A[0]+k-A[-1]
for i in range(1,n):
    mdist = max(A[i]-A[i-1],mdist)

print(k-mdist)