import heapq as hq

# Write a Python program to push elements and pop off the smallest one.
heap = []

for i in [50,47,23,56]:
    hq.heappush(heap, i)
# print(heap)

hq.heappushpop(heap, 45)
print(heap)

hq.heappushpop(heap, 70)
print(heap)

