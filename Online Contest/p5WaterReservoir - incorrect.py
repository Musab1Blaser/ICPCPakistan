def largeMax(lst, startPos):
    maxVal = lst[startPos]
    maxInd = startPos
    for i in range(startPos, len(lst)):
        if lst[i] > maxVal:
            maxInd = i
            maxVal = lst[i]
    return maxInd

def check(lst, mid):
    global breaks
    pos = mid
    length = len(lst)
    while pos != length-1:
        # print(lst[pos+1:])
        pos = largeMax(lst, pos+1)
        breaks.append(pos)

def checkVal(lst, breaks):
    ind = 0
    val = 0
    maxVal = 0
    while ind < len(breaks) -1:
        minHeight = heights[breaks[ind+1]]
        for bar in range(breaks[ind] + 1, breaks[ind+1]):
            val += minHeight - lst[bar]
        maxVal = max(maxVal, val)
        # print(val)
        val = 0
        ind += 1
    return maxVal


l = int(input())

hei = list(map(int, input().strip().split()))
heights = []
pos = 0
while hei[pos] <= hei[pos+1]:
    pos += 1
endPos = len(hei) - 1
while hei[endPos] <= hei[endPos - 1]:
    endPos -= 1
heights = hei[pos:endPos+1]
# print(heights)

maxVal = 0
midPoint = heights.index(max(heights))
breaks = [midPoint]
check(heights, midPoint)
maxVal = max(checkVal(heights, breaks), maxVal)

# print(checkVal(heights, breaks))

heights.reverse()
midPoint = heights.index(max(heights))
breaks = [midPoint]
check(heights, midPoint)
maxVal = max(checkVal(heights, breaks), maxVal)


print(maxVal)



