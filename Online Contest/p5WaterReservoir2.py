# l = int(input().strip())
heights = list(map(int, input().strip().split()))

ind = 0
while ind < len(heights)-1 and heights[ind+1] > heights[ind]:
    ind += 1
# print(ind)

prevMax = heights[ind]
maxHeight = 0
totalH = 0
while ind < len(heights)-1:
    prevMax = heights[ind]
    nextMax = max(heights[ind+1:])
    value = 0
    hei = min(nextMax, prevMax)
    ind += 1
    while ind < len(heights) and heights[ind] < prevMax and heights[ind] != nextMax:
        value += hei - heights[ind]
        ind += 1
    # maxHeight = max(maxHeight, value)
    totalH += value
print(totalH)
        

