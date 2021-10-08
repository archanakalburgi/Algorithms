'''
Let's say the string word is an occurrence of the string sequence if sequence contains word as a substring.
Let's say the string word is a k-occurrence of the string sequence if sequence contains word repeated k times as a
substring. Note that if word is an occurrence of sequence , it is a 1-occurrence as well.
For example, if word = "ab" and sequence = "dabcacab" then word is a 1-occurrence of sequence but not a 2
occurrence, because sequence doesn't contain "abab" as a substring. On the other hand, the string "ca" is a 2
occurrence of sequence , since it contains "caca" as a substring.
Given a string sequence and an array of strings words , your task is to find the maximal value of k for each element,
such that words [i] is a k-occurrence of sequence Return the k-values as an array of integers of length
words. length

Example
For sequence = "ababcbabc" and words = ["ab", "babc", "bca"] , the output should be
maxK0ccurrences (sequence, words) = [2, 2, 0] .
• words[0] = "ab" is a 2-occurrence of sequence because sequence[0..4] = "abab"
• words[0] = "ab" is not a 3-occurence of sequence , because there is no substring "ababab" in
sequence
words[1] = "babc" is a 2-occurrence of sequence , because sequence[1..8] = "babcbabe"
words[1] = "babc" is not a 3-occurence of sequence , because there is no substring "babcbabcbabc" in
sequence ;
words[2] = "bca" is a 0-occurrence of sequence because there is no substring "bca" in sequence
'''

def helper( sequence, word):
    count = 1
    while word*count in sequence:
        count += 1
    return count-1

def maxKOccurrences (sequence, words):
    result = list()
    for word in words:
        result. append (helper (sequence, word))
    return result
