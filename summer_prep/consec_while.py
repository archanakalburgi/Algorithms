def count_cc(string, integer):
    p1, p2 = 0,0
    result = ''
    while p2<len(string):
        if string[p1] == string[p2]:
            p2+=1
            if p2 <= integer:
                result+=string[p1:p2+1]
        else:
            p1 = p2
            p2 += 1
    return result

string = 'aabbbccccaaaaa'
integer = 2
print(count_cc(string, integer))
