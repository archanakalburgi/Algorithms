'''
Given an array of integers a your task is to calculate the digits that occur the most number of times in the array.
Return the array of these digits in ascending order.

Example
For a = [25, 2, 3, 57, 38, 41] , the output should de
mostFrequentDigits(a) = [2, 3, 5].

Here are the number of times each digit appears in the array:

0-1
1-1
2-2
3-2
4-1
5-2
6-0
7-1
8-1

The most number of times any number occurs in the array is 2 and the digits which appear 2 times are 2,3 and 5.
So the answer is [2, 5, 5]
'''
import collections
# from collections import Counter
def mostFrequentDigits(a):
    d = dict()
    sorted_d = collections.OrderedDict()
    for num in a:
        if num > 9:
            num = str(num)
            for i in range(len(num)):
                if int(num[i]) in d:
                    d[int (num [i])] += 1
                else:
                    d[int (num [i])] = 1
        else:
            if num in d:
                d [num] += 1
            else:
                d [num] = 1

    sorted_d = sorted(d.items(), key=lambda item: item[1], reverse=True)

    return sorted_d


def most_frequent_digits(a):
    digits = collections.Counter()
    numbers = list()
    for num in a:
        while num >= 9:
            numbers.append(num%10)
            num = num//10
        numbers.append(num)

    for n in numbers:
        digits[n] += 1 
    m_cmn = digits.most_common(1)[0][1] # nlogn
    cmp = collections.defaultdict(list)
    for k, v in digits.items():
        cmp[v].append(k)
    return(sorted(cmp[m_cmn]))


a = [25, 2, 3, 57, 38, 41]
print(most_frequent_digits(a))
