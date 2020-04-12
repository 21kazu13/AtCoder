import numpy as np
n = int(input())
l = []
for i in range(n):
    l.append(list(input()))

ans = np.array(l).T.tolist()
for i in ans:
    print(''.join(i[::-1]))
