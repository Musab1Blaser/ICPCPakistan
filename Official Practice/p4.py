for __ in range(int(input())):
    bill,amount=map(int, input().split())
    change=amount-bill
    lst=[]
    print(str(change)+':',end=' ')
    denominations=[5000,1000,500,100,50,20,10,5,2,1]
    for i in denominations:
        while change>=i:
            lst.append(i)
            change=change-i
    newlst=[]
    for i in denominations:
        newlst.append('('+str(i)+'x'+str(lst.count(i))+')')
    print(' + '.join(newlst))