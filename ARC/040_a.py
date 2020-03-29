def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))

red = 0
blue = 0
n = ii()
for i in range(n):
    s = input()
    for item in s:
        if item == 'R':
            red += 1
        elif item == 'B':
            blue += 1
if red > blue:
    print('TAKAHASHI')
elif blue > red:
    print('AOKI')
else:
    print('DRAW')