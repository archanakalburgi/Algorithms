import heapq as hq

heap = [0]
for element in [40,10,50,20]:
    hq.heappush(heap, element)
print(heap)
print(hq.heappop(heap))
print(heap)
print(hq.heappushpop(heap, 45))
print(heap)


heap2 = [78, 34, 78, 11, 45, 13, 99]
print(heap2)
hq.heapify(heap2)
print(heap2)

print(hq.heapreplace(heap2, 12))
print(heap2)

print(hq.heapreplace(heap2, 100))
print(heap2)



def is_even(num):
    if num%2 == 0: return 1
    return 0

heap = [78, 34, 78, 11, 45, 13, 99]
hq.heapify(heap2)
print("heap: ", heap2)

out = hq.nlargest(2, heap2, is_even)
print(out)


print(hq.nlargest(2, heap2))