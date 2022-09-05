import re

t = int(input())
while t:
    t -= 1
    txt = input()
    n = int(input())
    strs = [input() for x in range(n)]

    # print("---------------\nTest case: ", t)
    # print("n - ", n)
    # print("Strings - ", strs)

    
    indices = [[i.start() for i in re.finditer("(?="+s+")", txt)] for s in strs]
    tot = 0
    for i in indices:
        tot += len(i) 
    
    if tot == 0:
        print(-1)
        continue
    dp = [['' for _ in range(len(txt) + 1)] for _ in range(tot)]
    # Initialize dp matrix

    for i in range(len(dp)):
        dp[i][0] = 0

    
    cnt = 0
    for i in range(len(indices)):
        for j in range(len(indices[i])):
            for k in range(indices[i][j], len(strs[i]) + indices[i][j]):
                dp[cnt][1+k] = strs[i][k - indices[i][j]]
            cnt += 1

    # print(indices)
    # print()
    mncol = {}
    mncol[0] = 0
    sol = None
    
    for col in range(1, len(dp[0])):
        mn = None
        exist = False
        for row in range(len(dp)):
            if dp[row][col]:
                exist = True
                if dp[row][col - 1]:
                    dp[row][col] = dp[row][col - 1]
                else:
                    dp[row][col] = mncol[col - 1] + 1
                if mn is None:
                    mn = dp[row][col]
                else:
                    mn = min(mn, dp[row][col])

        if not exist:
            sol = -1
            break
        mncol[col] = mn

            

    print("-------")
    for row in dp:
        for i, v in enumerate(row):
            if row[i] == '':
                row[i] = 0

    for r in dp:
        print(r)

    if sol is None:
        print(mncol[len(dp[0]) - 1])
    else:
        print(-1)
    print("--------")


# 6
# bababa
# 2
# ba
# aba
# caba
# 2
# bac
# acab
# abacabaca
# 3
# aba
# bac
# aca
# baca
# 3
# a
# c
# b
# codeforces
# 4
# def
# code
# efo
# forces
# aaaabbbbcccceeee
# 4
# eeee
# cccc
# aaaa
# bbbb
