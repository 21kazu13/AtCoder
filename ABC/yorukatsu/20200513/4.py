import re
s = input()
s = re.sub('eraser','0',s)
#print(s)
s = re.sub('erase','0',s)
#print(s)
s = re.sub('dreamer','0',s)
#print(s)
s = re.sub('dream','0',s)
#print(s)


print('YES' if set(s) == set('0') else 'NO')