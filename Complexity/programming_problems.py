'''1. Write a recursive function called intpow that given a number, x, and an integer, n,
will compute x ^ n. You must write this function recursively to get full credit. Be
sure to put it in a program with several test cases to test that your function works
correctly.'''

# def intpow(x, n):
#     if(n==1):
#         return(x)
#     if(n!=1):
        
#         return (x*intpow(x,n-1))
# print(intpow(2,4))
    

''' 2. Write a recursive function to compute the factorial of an integer. The factorial of
0 is 1. The factorial of any integer, n, greater than zero is n times the factorial
of n−1. Write a program that tests your factorial function by asking the user to
enter an integer and printing the factorial of that integer. Be sure your program
has a main function. Comment your code with the base case and recursive case
in your recursive function.
'''
# def factorial(n):
#     if n == 0:
#         return 1 # base case, it has to stop when n becomes zero 
#     else:
#         return n * factorial(n-1) # recursion : n * (n-1)

# def main():
#     fact = factorial(int(input('Enter the number : ')))
#     print(fact) 

# if __name__ == "__main__":
#     main()  


'''3. Write a recursive function that computes the length of a string. You cannot use
the len function while computing the length of the string. You must rely on the
function you are writing. Put this function in a program that prompts the user to
enter a string and then prints the length of that string. '''

# def length_of_string(word, count = 0):
#     if word :
#         count = count + 1
#         return (length_of_string(word[1:], count))
#     else :
#         return count

# print(length_of_string(''))
# print(length_of_string('archana'))

''' 4. Write a recursive function that takes a string like “abcdefgh” and returns “badcfehg”.
Call this function swap since it swaps every two elements of the original
string. Put this function in a program and call it with at least a few test cases.'''

# i/p = 'abcdefgh'
# o/p = “badcfehg”

def swap(string):
    if string :
        return string[1]+ string[0]+ swap(string[2:]) 
    else :
        return string

print(swap('abcdefgh')) 
print(swap('abcd'))
print(swap('ab'))

# o/p :
# badcfehg
# badc
# ba