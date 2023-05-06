ヒープソートを行うコードです。<br>



```Python
import heapq
import random

def heap_sort(array):
    
    heap = []
    
    for v in array:
        heapq.heappush(heap,v)
    
    return [heapq.heappop(heap) for i in range(len(heap))]
    

array = [random.randint(0,6000) for i in range(6000)]
print(heap_sort(array))
```
