''' Write a Python program to perform Heap Sort, push all items to a heap, 
and then take off the smallest ones one after other. '''
import heapq as hq

heap = []
for i in [50,47,23,56]:
    hq.heappush(heap, i) 

hq.heapify(heap)

for _ in range(len(heap)):
    print(hq.heappop(heap)) 