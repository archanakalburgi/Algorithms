'''
Question: Remove the consecutive character from a given string if the number of consecutive characters exceeds the given integer 
'''
import collections
from typing import Collection, OrderedDict
def count_cc1(string):
    # char_count = OrderedDict()
    char_count = collections.Counter(OrderedDict())
    for letter in string:
        char_count[letter] += 1
    return char_count

def count_cc2(string):
    p1, p2 = 0,0
    result_list = []
    for i in range(1,len(string)):
        if string[i-1] == string[i]:            
            p2=i
        else:
            result_list.append(string[p1:p2+1]) 
            p1 = i
            p2 = i
            # print(p1,p2)
    result_list.append(string[p1:len(string)])
    return result_list

def count_cc3(string): # works for repeating consecutive character 
    temp_list = list()
    count = 1
    for i in range(1,len(string)):
        if string[i-1] == string[i]:
            count = count+1
        else:
            temp_list.append((string[i-1], count))
            count = 1
    temp_list.append((string[-1],count))
    return temp_list

def consecutive_character(string, integer):
    result = ''
    temp_list = count_cc3(string)
    for tup in temp_list:
        result += tup[0]*min(tup[1], integer)
    print(temp_list)
    return result

'''
s = len(string)
t: O(s)+O(s)
t: O(s)+O(s)+O(s)
'''

string = 'aabbbccccaa'
# print(consecutive_character('aabbbccc', 2))
print('\n')
print("ordered dictionary: ",count_cc1(string)) 
print('\n')
print("list of consecutive letters: ",count_cc2(string)) # [aa, bbb, cccc]
print('\n')
print("list of tuples: ",count_cc3(string))
print('\n')
