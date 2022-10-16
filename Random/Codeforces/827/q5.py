def find_index(arr, n, K):

    start = 0
    end = n - 1

    while start<= end:
 
        mid =(start + end)//2
 
        if arr[mid] == K:
            return mid
 
        elif arr[mid] < K:
            start = mid + 1
        else:
            end = mid-1

    return end + 1

t = int(input())
while t:
    t -= 1
    n, q = map(int, input().split())
    arr = list(map(int, input().split()))
    ques = list(map(int, input().split()))

    myarr = []
    mx = -1
    sm = 0
    d={}
    for i in arr:
        sm += i
        if i > mx:
            
            myarr.append(i)
            mx = i
        d[mx] = sm
    
    sol = []
    for k in ques:
        res = find_index(myarr, len(myarr), k)
        if res < len(myarr):
            if k == myarr[res]:
                sol.append(str(d[myarr[res]]))
            else:
                if res - 1 >= 0:
                    sol.append(str(d[myarr[res - 1]]))
                else:
                    sol.append("0")
        else:
            sol.append(str(d[myarr[res - 1]]))
    print(" ".join(sol))

# a= find_index([1], 1, 0)
# print(a)
