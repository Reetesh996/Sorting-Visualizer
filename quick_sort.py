def partition(y,low,high):
    pivot=y[low]
    i=low+1
    j=high
    while True:
        while i<=j and y[i]<=pivot:
            i+=1
            yield y
        while i<=j and y[j]>pivot:
            j-=1
            yield y
        if i<j:
            y[i],y[j]=y[j],y[i]
        else:
            break
    y[low],y[j]=y[j],y[low]
    yield y
    return j


def quicksort(y,low,high):
    if low<high:
        j=yield from partition(y,low,high)
        yield from quicksort(y,low,j-1)
        yield from quicksort(y,j+1,high)
