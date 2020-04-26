import re 
s = input()
ans = ['Fa','Mi',2,'Re',4,'Do','Si',7,'La',9,'So']
m = re.search('WBWBWBW',s)
print(ans[m.start()])