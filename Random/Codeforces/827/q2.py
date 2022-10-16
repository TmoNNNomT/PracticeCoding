t = int(input())
while t:
    t -= 1
    n = int(input())
    arr = list(map(int, input().split()))
    if len(arr) == len(set(arr)):
        print("YES")
    else:
        print("NO")