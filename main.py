import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import matplotlib.cm as cm
from matplotlib.colors import Normalize
from bubble_sort import bubblesort
from selection_sort import selectionsort
from insertion_sort import insertionsort
from merge_sort import mergesort
from quick_sort import quicksort
from heap_sort import heapsort


if __name__=="__main__":
    while True:
        n=int(input(" How many Numbers: "))
        
        print('1. Bubble Sort')
        print('2. Selection Sort')
        print('3. Insertion Sort')
        print('4. Merge Sort')
        print('5. Quick Sort')
        print('6. Heap Sort')
        ch=int(input("Enter your choice: "))
        
        y = np.random.randint(1,n+1,n)
        fig,axes = plt.subplots()
        
        if ch==1:
            title='BUBBLE SORT O(n**2)'
            generator = bubblesort(y)
        elif ch==2:
            title='SELECTION SORT O(n**2)'
            generator = selectionsort(y)
        elif ch==3:
            title='INSERTION SORT O(n**2)'
            generator = insertionsort(y)
        elif ch==4:
            title='MERGE SORT O(n*log(n))'
            generator = mergesort(y,0,n-1)
        elif ch==5:
            title='QUICK SORT O(n*log(n))'
            generator = quicksort(y,0,n-1)
        elif ch==6:
            title='HEAP SORT O(n**log(n))'
            generator = heapsort(y,n)
            
        mycmap= cm.get_cmap('rainbow')
        
        my_norm = Normalize(vmin=0, vmax=100)
        
        
        barr = axes.bar(np.arange(1,n+1),y,align='edge',color=mycmap(my_norm(y)))
        axes.set_xticks(range(0,n+1,n//5))
        axes.set_yticks(range(0,n+1,n//5))
        text = axes.text(0.02, 0.95, "", transform=axes.transAxes)
        axes.set_title(title)
        
        count=0
        def outp(y,r):
            global count
            for a,b in zip(r,y):
                a.set_height(b)
            count+=1
            text.set_text("Number of Operations: "+str(count))
        
        anim = FuncAnimation(fig, outp, fargs=(barr,) ,frames = generator, interval=5, repeat=False)
        plt.show()
        ct = input("DO YOU WISH TO CONTINUE(y/n): ")
        if ct!='y' and ct!='Y':
            break
