s = list(input())

#sは回文
for i in range(len(s)//2):
    if s[i] != s[-i-1]:
        print('No')
        exit()

#Sの1文字目から(N−1)/2 文字目まで(両端含む)からなる文字列は回文
s_begin = s[:len(s)//2:]
for j in range(len(s_begin)//2):
    if s_begin[j] != s_begin[-j-1]:
        print('No')
        exit()

#Sの(N+3)/2文字目からN文字目まで(両端含む)からなる文字列は回文
s_end = s[len(s)//2+1::]
for k in range(len(s_end)//2):
    if s_end[k] != s_end[-k-1]:
        print('No')
        exit()

print('Yes')
