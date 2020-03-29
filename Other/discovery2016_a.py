s = 'DiscoPresentsDiscoveryChannelProgrammingContest2016'
n = len(s)
w = int(input())

for i in range((n+w-1)//w):
    print(s[:w])
    s = s[w:]