import re

s = input()
era = 'eraser'
er = 'erase'
dr = 'dream'
drm = 'dreamer'

#s1 = re.sub(era,'',s)
#s2 = re.sub(er,'',s1)
#s3 = re.sub(drm,'',s2)
#s4 = re.sub(dr,'',s3)
s1 = re.sub(era,'0',s)
s2 = re.sub(er,'0',s1)
s3 = re.sub(drm,'0',s2)
s4 = re.sub(dr,'0',s3)

#if s4 == '':
if re.sub('0','',s4) == '':
    print('YES')
else:
    print('NO')