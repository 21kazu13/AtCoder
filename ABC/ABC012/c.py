n = int(input())
for i in range(1,10):
    for j in range(1,10):
        if 2025 - n == i*j:
            print('{} x {}'.format(i,j))