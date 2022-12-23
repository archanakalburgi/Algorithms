def printPattern(n):
    for i in range(5):
        for j in range(i+1):
            print(1, end="")
        print("")
    for k in range(6, 0, -1):
        for l in range(k-1):
            print(2, end="")
        print("")

printPattern(5)