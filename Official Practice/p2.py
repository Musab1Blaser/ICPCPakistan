
def bfs(start, end, occupied):
    visited = set()
    opts = [[-2, -1], [-2, 1], [-1, -2], [-1, 2], [2, -1], [2, 1], [1, -2], [1, 2]]
    moves = 0
    toExplore = {start}
    while len(toExplore) > 0:
        newExplore = set()
        moves += 1
        for pos in toExplore:
            for opt in opts:
                nextPos = (pos[0] + opt[0], pos[1] + opt[1])
                if nextPos not in toExplore and nextPos not in visited and nextPos[0] <= 7 and nextPos[0] >= 0 and nextPos[1] <= 7 and nextPos[1] >= 0 and nextPos not in occupied:
                    newExplore.add(nextPos)
                    if nextPos == end:
                        return moves
            visited.add(pos)
        toExplore = newExplore.copy()
            
            


t = int(input())

for test in range(t):
    temp = list(map(int, input().strip().split()))
    startPos = (temp[0], temp[1])
    endPos = (temp[2], temp[3])
    occupied = int(input())
    occupiedPos = set()
    temp = list(map(int, input().strip().split()))
    for i in range(occupied):
        occupiedPos.add((temp[2*i], temp[2*i + 1]))

    # print(startPos)
    # print(endPos)
    # print(occupiedPos)

    x = bfs(startPos, endPos, occupiedPos)
    print(f"Case {test+1}:", x)