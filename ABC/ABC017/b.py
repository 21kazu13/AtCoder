import re
s = input()

def isChoku(s):
    st = re.sub('ch$|o$|k$|u$','',s)
#    print(st=='')
    if st == '':
#        print('hoge')
        return True
    elif st == s:
        return False
    else:
        return isChoku(st)

print('YES' if isChoku(s) else 'NO')