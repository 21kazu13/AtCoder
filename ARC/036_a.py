def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
n,k = iim()
st = []
for i in range(n):
    st.append(ii())

for i in range(2,n):
    if st[i]+st[i-1]+st[i-2] < k:
        print(i+1)
        exit()

print(-1)