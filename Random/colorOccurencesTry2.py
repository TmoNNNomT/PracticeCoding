def main():
    tt = int(input())
    while tt:
        tt -= 1
        txt = input()
        n = int(input())
        strs = [input() for _ in range(n)]

        print("strs: ", strs)
        d = {}

        for i in range(len(txt)):
            d[i] = (-1, -1)
            for j in range(n):
                l = len(strs[j])
                if i + l <= len(txt) and strs[j] == txt[i:i+l]:
                    if d[i][1] < i + l:
                        d[i] = (j, i + l)

        print(d)
        
        p = 0
        res = []
        while p < len(txt):
            f = -1
            mx = -1
            for i in range(0, p+1):
                if mx < d[i][1]:
                    f, mx = i, d[i][1]
            if mx < p:
                print(-1)
                break

            res.append([d[f][0], p])
            p = mx + 1

        print(len(res))
        for r in res:
            print(r[0], r[1])
            




main()