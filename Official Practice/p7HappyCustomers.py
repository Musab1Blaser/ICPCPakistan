N, D = list(map(int, input().strip().split()))
A, B = list(map(int, input().strip().split()))


customers = []
for i in range(N):
    a, b = list(map(int, input().strip().split()))
    dates = A*a + B*b
    customers.append([dates, i+1])

customers.sort()
indexList = [str(i[1]) for i in customers]
# print(customers)
remDates = D
ind = 0
while remDates > 0 and ind < N:
    remDates -= customers[ind][0]
    ind += 1

# print(remDates)
if remDates < 0:
    ind -= 1
print(ind)
print(" ".join(indexList[:ind]))
