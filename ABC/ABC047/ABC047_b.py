w, h, n = map(int,input().split())
Op = []
for i in range(n):
    Op.append(list(map(int,input().split())))

Op1 = [0]
Op2 = [w]
Op3 = [0]
Op4 = [h]
for j in range(n):
    if Op[j][2] == 1:
        Op1.append(Op[j][0])
    elif Op[j][2] == 2:
        Op2.append(Op[j][0])
    elif Op[j][2] == 3:
        Op3.append(Op[j][1])
    elif Op[j][2] == 4:
        Op4.append(Op[j][1])
'''
print(Op1)
print(Op2)
print(Op3)
print(Op4)
'''
if min(Op2)-max(Op1) < 0:
    print(0)
elif min(Op4)-max(Op3) < 0:
    print(0)
else:
    print((min(Op2)-max(Op1))*(min(Op4)-max(Op3)))