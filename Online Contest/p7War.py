def makeGroups(powerList):
    groups = [[powerList[0]]]
    for i in range(1, len(powerList)):
        if powerList[i] > powerList[i-1] + 1:
            groups.append([powerList[i]])
        else:
            groups[-1].append(powerList[i])
    return groups

def sumGroups(group):
    evenSum = 0
    totalSum = sum(group)
    for elem in group:
        if (elem % 2) == 0:
            evenSum += elem
    return max(totalSum - evenSum, evenSum)

t = int(input())

for test in range(t):
    n = int(input())
    powerList = list(map(int, input().split()))
    powerList.sort()
    groups = makeGroups(powerList)
    # print(groups)
    curSum = 0
    for group in groups:
        curSum += sumGroups(group)
    print(curSum)
