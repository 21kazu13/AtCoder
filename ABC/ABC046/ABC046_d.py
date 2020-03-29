s = list(input())
countg = 0
countp = 0
for i in s:
    if i == 'g':
        countg += 1
    else:
        countp += 1

print(int((countg-countp)/2))