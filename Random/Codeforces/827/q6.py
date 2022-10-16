t = int(input())
while t:
    t-= 1
    q = int(input())
    strs = ["a", "a"]
    mn = "a"
    mx = "a"
    st1 = set("a")
    st2 = set("a")
    while q:
        q -= 1
        ind, x, txt  = input().split()
        ind = int(ind) - 1
        x = int(x)
        if ind == 0:
            mn = min(mn + txt)
            st1 = st1.union(set(txt))
        else:
            mx = max(mx + txt)
            st2 = st2.union(set(txt))
        
        strs[ind] += txt * x
        # print("NEW: ", strs)
        if strs[0] < strs[1]:
            print("YES")
        elif strs[0] == strs[1]:
            print("NO")
        elif mn < mx:
            print("YES")
        elif mn == mx and len(strs[0]) < len(strs[1]) and len(st1) == 1 and len(st2) == 1:
            print("YES")
        else:
            print("NO")
        