def bubblesort(y):
    for i in range(len(y)):
        for j in range(len(y)-i-1):
            if y[j]>y[j+1]:
                y[j],y[j+1]=y[j+1],y[j]
            yield y
            
