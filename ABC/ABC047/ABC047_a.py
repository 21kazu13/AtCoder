A = list(map(int,input().split()))

As = sorted(A)
if As[2] == As[1]+As[0]:
    print("Yes")
else:
    print("No")