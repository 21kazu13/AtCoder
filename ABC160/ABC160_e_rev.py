x, y, a, b, c = map(int,input().split())
red = sorted(list(map(int,input().split())),reverse=True)[:x]
green = sorted(list(map(int,input().split())),reverse=True)[:y]
white = sorted(list(map(int,input().split())),reverse=True)

l = sorted(red+green+white,reverse=True)[:x+y]
print(sum(l))
