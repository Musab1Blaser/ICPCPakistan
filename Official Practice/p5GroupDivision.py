t = int(input())

for test in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    nums.sort(reverse=True)
    totalSum = sum(nums)
    curSum = 0
    for i in range(0, len(nums), 2):
        curSum += nums[i]
    if len(nums)%2 == 1:
        curSum -= nums[-1]
    print(curSum)
    print(totalSum - curSum)
