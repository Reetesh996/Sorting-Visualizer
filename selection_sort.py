def selectionsort(y):
    for i in range(len(y)):
        pos=i
        for j in range(i+1,len(y)):
            if y[j]<y[pos]:
                pos=j
            yield y
        y[i],y[pos]=y[pos],y[i]
        yield y
 
