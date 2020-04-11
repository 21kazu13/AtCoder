s = input()
if s[0] != 'A':
    print('WA')
elif s[2:-1:].count('C') != 1:
    print('WA')
else:
    l = list(s[1::])
    l.remove('C')
    st = ''.join(l)
    if st == st.lower():
        print('AC')
    else:
        print('WA')