class Solution:
    def isAlienSorted(self, words, order):
        rules = dict()
        for i,letter in enumerate(order):
            rules[letter] = i 
        
        for i in range(len(words)-1):
            current_word = words[i]
            next_word = words[i+1]
            if len(current_word) > len(next_word): 
                return False
            for j in range(len(current_word)): 
                if current_word[j] != next_word[j]: 
                    if rules[current_word[j]] > rules[next_word[j]]:
                        return False
                    else:
                        break
        return True