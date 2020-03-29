import re
s = input()
s = re.sub('a|i|u|e|o','',s)
print(s)