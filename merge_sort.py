def merge(y,low,mid,high):
    m=mid-low+1
    n=high-mid
    A=[0]*m
    B=[0]*n
    for i in range(m):
        A[i]=y[low+i]
    for j in range(n):
        B[j]=y[mid+1+j]
    i=j=0
    k=low
    while i<m and j<n:
        if A[i]<B[j]:
            y[k]=A[i]
            i+=1
        else:
            y[k]=B[j]
            j+=1
        k+=1
        yield y
    while i!=m:
        y[k]=A[i]
        i+=1
        k+=1
        yield y
    while j!=n:
        y[k]=B[j]
        j+=1
        k+=1
        yield y
        
    
    
            
def mergesort(y,low,high):
    if low<high:
        mid=(low+high)//2
        yield from mergesort(y,low,mid)
        yield from mergesort(y,mid+1,high)
        yield from merge(y,low,mid,high)
        yield y
