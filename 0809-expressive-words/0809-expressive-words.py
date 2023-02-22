class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def getStack(word):
            stack = []
            for i in word:
                if stack and stack[-1][0] == i:
                    stack[-1] += i
                else:
                    stack.append(i)
            return stack
        main, result = getStack(s), 0
        for wrd in words:
            word = getStack(wrd)
            if len(word) != len(main): 
                continue
            for i in range(len(word)):
                if  len(word[i]) > len(main[i]) or not (word[i][0] == main[i][0] and (len(main[i]) == len(word[i]) or len(main[i]) >= 3)):
                    break
                if i == len(word) - 1:
                    result += 1
        return result
'''
"dddiiiinnssssssoooo"
["dinnssoo","ddinso","ddiinnso","ddiinnssoo","ddiinso","dinsoo","ddiinsso","dinssoo","dinso"]
'''