import re
w = input()
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for item in alphabet:
    pattern = item
    if len(re.findall(pattern, w))%2 == 1:
        print('No')
        exit()
print('Yes')
