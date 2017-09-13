def INSERT(L,N,Data):
    if Data < L[0]:
        pos = 0
    elif Data > L[N-1]:
        pos = N
    else:
        for i in range(0,N-1):
            if Data>=L[i] and Data <=L[i+1]:
                pos = i+1
                break
    L.append(0)

    for i in range(N,pos,-1):
        L[i] = L[i-1]
    L[pos] = Data

        
List = []
n = input("Enter size of list:- ")
print "Enter",n,"no. is ascending order"
for i in range(n):
    List.append(input(":- "))
print "Original List contents are:- ",List
D = input('Enter data to insert:- ')
INSERT(List,n,D)
print 'List contents after insertion are:- '
for i in range(0,n+1):
    print List[i],

