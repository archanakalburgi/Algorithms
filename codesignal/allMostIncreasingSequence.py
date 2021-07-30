# def almostIncreasingSequence(sequence): 
#     for i in range(len(sequence)):
#         count = 0
#         for j in range(i):
#             if sequence[i] - sequence[j] < 0:
#                 count = count + 1 
#     print(count)
#     if count == 1 : 
#         return True
#     return False

# def almostIncreasingSequence(sequence): 
#     for i in range(len(sequence)):
#         if sequence[i] > sequence[i+1]:
#             if sequence[i+2] - sequence[i] < 0 and sequence[i+1] < sequence[i-1]:
#                 return False
#     return True
       
def almostIncreasingSequence(sequence): 
    def helper(a,b):
        return a > b 
        
    booleans = []
    for i in range(len(sequence)-1):
        booleans.append(helper(sequence[i], sequence[i+1]))
    
    # print(booleans)
    # print(booleans.count(True))
    if booleans.count(True) > 1:
        return False 
    


sequence = [1, 3, 2, 1] 
print(almostIncreasingSequence(sequence))