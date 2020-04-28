from math import ceil
def heapsort(y,n):
    size=n
    for i in range(n):
        yield from restoreup(y,i,n)
        yield y
    size=n-1
    while size!=0:
        y[0],y[size]=y[size],y[0]
        size-=1
        yield from restoredown(y,0,size)
        yield y
    yield y
    
        
def restoreup(y,i,n):
    if i==0:
        return
    while True:
        parent=ceil(i/2)-1
        if y[parent]<y[i] and parent>-1:
            y[i],y[parent]=y[parent],y[i]
            i=parent
        else:
            break
        yield y

def restoredown(y,i,size):
    while 2*i+2<=size:
        left=2*i+1
        right=2*i+2
        if y[left]>=y[right]:
            ans=left
        else:
            ans=right
        if y[ans]>y[i]:
            y[ans],y[i]=y[i],y[ans]
            i=ans
        else:
            break
        yield y
    if 2*i+1==size and y[i]<y[2*i+1]:
        y[i],y[2*i+1]=y[2*i+1],y[i]
    yield y
    
