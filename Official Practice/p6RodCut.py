t = int(input().strip())

def dp(curCost, curVal, M):
    global optimalM
    

for test in range(t):
    optimalM = [0] *501
    vals = list(map(int,input().strip().split()))
    M = vals[0]
    for item in range(1, M+1):
        curVal = vals[item]
        for budget in range(M+1):
            if item <= budget:
                optimalM[budget] = max(optimalM[budget], optimalM[budget-item] + curVal)
    print(max(optimalM))
        # M[i] = max(M[i], dp(, val, i))
