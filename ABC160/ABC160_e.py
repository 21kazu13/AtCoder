x, y, a, b, c = map(int,input().split())
red = sorted(list(map(int,input().split())))[::-1]
green = sorted(list(map(int,input().split())))[::-1]
white = sorted(list(map(int,input().split())))[::-1]
rcnt = 0
rflag = x-1
gcnt = 0
gflag = y-1
wcnt = 0
ans = 0
#print(red,green,white)
red.append(0)
green.append(0)
white.append(0)

for i in range(x+y):
    print(i,red,green,white)    
    if red[rcnt] == max(red[rcnt],green[gcnt],white[wcnt]):
#        print('hoge')
        ans += red[rcnt]
        rcnt += 1
    elif green[gcnt] == max(red[rcnt],green[gcnt],white[wcnt]):
#        print('huga')
        ans += green[gcnt]
        gcnt += 1
    else:
        if red[rflag] < green[gflag]:
            rcnt += 1
            rflag -= 1
        else:
            gcnt += 1
            gflag -= 1
#        print('foo')
        ans += white[wcnt]
        wcnt += 1
    print(ans)