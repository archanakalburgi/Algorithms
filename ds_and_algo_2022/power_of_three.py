
def isPowerOfThree(n: int) -> bool:
    print(n)
    
    if n==1:
        print("1",n)
        return True
    
    if n%3 != 0 or n == 0:
        print("2",n)
        return False
    
    return isPowerOfThree(n//3)
    print("hi" )

print(isPowerOfThree(27))