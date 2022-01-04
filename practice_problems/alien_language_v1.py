class Solution:
    def isAlienSorted(self, words, order):
        
        rules = dict()
        for i,letter in enumerate(order):
            rules[letter] = i 
        
        for i in range(len(words)-1):
            for j in range(len(words[i])):
                if j >= len(words[i+1]):
                    return False
                
                if words[i][j] != words[i+1][j]:
                    if rules[words[i][j]] > rules[words[i+1][j]]:
                        return False
                    else:
                        break
        return True

sol = Solution()
words=["kuvp","q"]
order="ngxlkthsjuoqcpavbfdermiywz"
print(sol.isAlienSorted(words, order))
