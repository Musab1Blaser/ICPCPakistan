t = int(input())

def createDict(map1, map2):
    mapDict = {}
    for ind in range(len(map1)):
        if map1[ind] not in mapDict:
            mapDict[map1[ind]] = [map2[ind]]
        else:
            mapDict[map1[ind]].append(map2[ind])
    return mapDict

def bfs(start, target, mapDict):
    visited = set()
    toVisit = {start}
    while len(toVisit) != 0:
        newVisit = set()
        for opt1 in toVisit:
            if opt1 in mapDict:
                for opt2 in mapDict[opt1]:
                    if opt2 == target:
                        return True
                    elif opt2 not in toVisit and opt2 not in visited and opt2 not in newVisit:
                        newVisit.add(opt2)
            visited.add(opt1)
        toVisit = newVisit.copy()
    return False

for test in range(t):
    map1 = input().split()
    map2 = input().split()
    mapDict = createDict(map1, map2)
    # print(mapDict)
    n = int(input())
    for pair in range(n):
        s1, s2 = input().split()
        if len(s1) == len(s2) and len(s1) >= 3 and len(s1) <=20 :
            for pos in range(len(s1)):
                if s1[pos] != s2[pos]:
                    if bfs(s1[pos], s2[pos], mapDict) == False:
                        print("No")
                        break
            else:
                print("Yes")
        else:
            print("No")
