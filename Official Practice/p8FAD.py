n = int(input())

for i in range(n):
    p = int(input())
    line = [0] * p
    ind = 0
    jump = 0
    while jump<p:
        line[ind] = 1
        jump += 1
        if jump >= p:
            break
        ind = (ind + 1) % p
        
        while line[ind] == 1:
                ind = (ind + 1) % p
        for j in range(jump):
            ind = (ind + 1) % p
            while line[ind] == 1:
                ind = (ind + 1) % p
    print(ind+1)
