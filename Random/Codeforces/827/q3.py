t = int(input())
while t:
    t -= 1
    grid = []
    tmp = input()
    for i in range(8):
        grid.append(input())
    # print(grid)
    red = True
    i, j = [0, 0]
    while i < 8 and j < 8:
        if grid[i][j]  not in ['R', 'B']:
            j += 1
        elif grid[i][j] == "R":
            if not red:
                j = 0
                red = True
                continue
            j += 1
        else:
            if red:
                i = 0
                red = False
                continue
            i += 1
    ans = "R" if red else "B"
    print(ans)
