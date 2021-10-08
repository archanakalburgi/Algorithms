def count_cc(string, integer):
    p1, p2 = 0,0
    result = ''
    for i in range(1,len(string)):
        if string[i-1] == string[i]:            
            p2=i+1 
            if (p2-p1) <= integer:
                result += string[i]
        else:
            result += string[i]
            p1 = i
            p2 = i
    return result

'''
t: O(s)
    iterate input string
s: O(s) 
    result string
'''

string = 'aabbbccccaaaaa'
integer = 2
print(count_cc(string,integer))