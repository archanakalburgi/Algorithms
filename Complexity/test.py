def pascal_triagle(rows):
    l = [1]
    for i in range(rows):
        print(l)
        newlist = []
        newlist.append(l[0])

        for i in range(len(l)-1):
            newlist.append(l[i] + l[i+1])

        newlist.append(l[-1])
        l = newlist  

pascal_triagle(4)

#no of steps = 46