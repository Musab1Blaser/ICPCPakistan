def inGrid(pos):
    global D
    # print(D)
    if pos[0] >= 0 and pos[0] < D and pos[1] >= 0 and pos[1] < D:
        return True
    else:
        return False

def bfs(grid, pos):
    white = 1
    visited = set()
    toVisit = {pos}
    while len(toVisit) != 0:
        newVisit = set()
        for point in toVisit:
            opts = [(point[0] + 1, point[1]), (point[0] - 1, point[1]), (point[0], point[1] + 1), (point[0], point[1]-1),   (point[0] + 1, point[1] + 1), (point[0] + 1, point[1] - 1), (point[0] - 1, point[1] + 1), (point[0] - 1, point[1]-1),]
            opts = list(filter(inGrid, opts))
            for opt in opts:
                if grid[opt[0]][opt[1]] == "W" and opt not in visited and opt not in toVisit and opt not in newVisit:
                    white += 1
                    newVisit.add(opt)
            visited.add(point)
        toVisit = newVisit.copy()
    return white



t = int(input())

#first index is row, second is column
for test in range(t):
    D, Q = list(map(int, input().strip().split()))
    grid = []
    for row in range(D):
        grid.append(input().strip())
    for q in range(Q):
        pos = tuple(map(int, input().strip().split()))
        pos = (pos[0]-1, pos[1] - 1)
        print(bfs(grid, pos))