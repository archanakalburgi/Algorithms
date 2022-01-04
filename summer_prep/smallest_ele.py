import heapq
def smallest_using_heap(array):
    array = [22,19,12,89,34,18,2,4,0,-8,-9]
    heapq.heapify(array) 
    print(heapq.nsmallest(2, array)[1])
    print(heapq.nlargest(2, array)[1])


def smallest_for_loop(array):
    array.sort()
    return array[:2]
        

from collections import OrderedDict
def smallest(array):
    result_temp = dict()
    for idx, num in enumerate(array):
        result_temp[idx] = num
    return sorted(result_temp.keys(), key= lambda k: result_temp[k])[:2]

array = [-8,-9,22,19,12,89,34,18,2,4,0]
print(smallest(array))
print(smallest_for_loop(array))