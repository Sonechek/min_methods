grid = [[1, 2, 6, 4], [3, 1, 3, 2], [5, 7, 5, 1]]
supply = [40, 30, 20, 3]
demand = [30, 25, 18, 20]
startR = 0
startC = 0
ans = 0

while startR != len(grid) and startC != len(grid[0]):
    if supply[startR] <= demand[startC]:
        ans += supply[startR] * grid[startR][startC]
        demand[startC] -= supply[startR]
        startR += 1
    else:
        ans += demand[startC] * grid[startR][startC]
        supply[startR] -= demand[startC]
        startC += 1

print(ans)
