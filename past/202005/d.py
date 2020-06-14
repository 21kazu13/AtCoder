'''
10
.###..#..###.###.#.#.###.###.###.###.###.
.#.#.##....#...#.#.#.#...#.....#.#.#.#.#.
.#.#..#..###.###.###.###.###...#.###.###.
.#.#..#..#.....#...#...#.#.#...#.#.#...#.
.###.###.###.###...#.###.###...#.###.###.
'''
def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
n = int(input())
l = [input() for _ in range(5)]
ans = []
#print(l)
for i in range(n):
    l0 = l[0][4*i:4*(i+1)]
    l1 = l[1][4*i:4*(i+1)]
    l2 = l[2][4*i:4*(i+1)]
    l3 = l[3][4*i:4*(i+1)]
    l4 = l[4][4*i:4*(i+1)]
#    print(l0)
#    print(l1)
#    print(l2)
#    print(l3)
#    print(l4)
    if l0 == '..#.':#1or4
        ans.append(1)
    elif l0 == '.#.#':
        ans.append(4)
    elif l1 == '.#..':#5or6
        if l3 == '...#':
            ans.append(5)
        else:
            ans.append(6)
    elif l1 == '...#': #2or3or7
        if l3 == '.#..':
            ans.append(2)
        elif l2 == '.###':
            ans.append(3)
        else:
            ans.append(7)
    else:#0or8or9
        if l3 == '...#':
            ans.append(9)
        elif l2 == '.#.#':
            ans.append(0)
        else:
            ans.append(8)
#    print(ans)

print(''.join(list(map(str,ans))))
