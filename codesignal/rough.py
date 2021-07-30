def almostIncreasingSequence(sequence):
    count1 = 0 
    count2 = 0
    count3 = 0

    for i in range(len(sequence)-1):
        if sequence[i] >= sequence[i+1] :
            count1 += 1
    
    for j in range(len(sequence)-2):
        if sequence[j] >= sequence[j+2]:
            count2+=1

    for k in range(len(sequence)-2):
        if sequence[k] >= sequence[k+2]:
            count3+=1

    return (count1 <=1) and (count2 <= 1) and (count3 <= 1)

print(almostIncreasingSequence([10,11,12,9,1]))