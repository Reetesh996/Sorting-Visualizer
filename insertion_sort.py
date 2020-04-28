def insertionsort(y):
    for i in range(1,len(y)):
        for j in range(i,0,-1):
            if y[j]<y[j-1]:
                y[j],y[j-1]=y[j-1],y[j]
            yield y
            
