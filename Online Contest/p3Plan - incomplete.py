def computeDist(n, aerials, path, moves):
    curPos = path[-1]
    goal = n-1
    endPos = curPos + 6
    opts = []
    for i in range(curPos+1, endPos):
        if i == n:
            return moves + 1
        if i in path:
            break
        if i in aerials:
            # print([aerials[i]])
            computeDist(n, aerials, path.extend([range(curPos+1, i)] + [aerials[i]]), moves + 1)
    if endPos in path:
        computeDist(n, aerials, path.extend(list(range(curPos+1, endPos))), moves + 1)



t = int(input())

for test in range(t):
    n = int(input())
    aerialR = int(input())
    aerials = {}
    for i in range(aerialR):
        source, dest = list(map(int, input().split()))
        aerials[source] = dest
    print(computeDist(n, aerials, [0], []))