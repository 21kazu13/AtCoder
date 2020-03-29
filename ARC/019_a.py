import re
s = input()
s = re.sub('O|D','0',s)
s = re.sub('I','1',s)
s = re.sub('Z','2',s)
s = re.sub('S','5',s)
s = re.sub('B','8',s)
print(s)