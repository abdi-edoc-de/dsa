class Solution:
    def values(self, s):
        if s in self.values_cache:
            return self.values_cache[s]
        if len(s)==1:
            self.values_cache[s] = [int(s),]
        elif len(s)==2:
            self.values_cache[s] = [int(s), int(s[0])+int(s[1])]
        elif len(s)==3:
            self.values_cache[s] = [int(s), int(s[0:2])+int(s[2]), int(s[0])+int(s[1:3]), int(s[0])+int(s[1])+int(s[2])]
        else:
            raise NotImplementedError
        return self.values_cache[s]
        
    def possiblyEqualsUtil(self, s1, s2, idx1, idx2, sum1, sum2):
        # print(s1[:idx1+1], sum1, s2[:idx2+1], sum2)
        if (idx1==-1 and sum1==0) and (idx2==-1 and sum2==0): # both s1 and s2 are exhausted means a match
            return True
        if (idx1==-1 and sum1==0) or (idx2==-1 and sum2==0): # either exhausted but other didn't
            return False
        if (idx1, idx2, sum1, sum2) in self.dp:
            return self.dp[(idx1, idx2, sum1, sum2)] 
        if sum1==0 and s1[idx1].isdigit(): # update sum1 when the idx1 is a digit and sum1 is 0
            next_idx1 = idx1
            while next_idx1>=0 and s1[next_idx1].isdigit():
                next_idx1 -= 1
            values1 = self.values(s1[next_idx1+1: idx1+1])
            answer = False
            for value1 in values1:
                answer = answer or self.possiblyEqualsUtil(s1, s2, next_idx1, idx2, value1, sum2)
            self.dp[(idx1, idx2, sum1, sum2)] = answer
        elif sum2==0 and s2[idx2].isdigit(): # update sum1 when the idx1 is a digit and sum1 is 0
            next_idx2 = idx2
            while next_idx2>=0 and s2[next_idx2].isdigit():
                next_idx2 -= 1
            values2 = self.values(s2[next_idx2+1: idx2+1])
            answer = False
            for value2 in values2:
                answer = answer or self.possiblyEqualsUtil(s1, s2, idx1, next_idx2, sum1, value2)
            self.dp[(idx1, idx2, sum1, sum2)] = answer
        else: # ready for comparisions
            if sum1 > 0 and sum2 > 0: # number-number compaision
                sum1, sum2 = sum1 - min(sum1, sum2), sum2 - min(sum1, sum2)
                self.dp[(idx1, idx2, sum1, sum2)] = self.possiblyEqualsUtil(s1, s2, idx1, idx2, sum1, sum2)
            elif sum1 > 0 and sum2 == 0 and s2[idx2].isalpha(): # number-alpha comparision
                self.dp[(idx1, idx2, sum1, sum2)] = self.possiblyEqualsUtil(s1, s2, idx1, idx2-1, sum1-1, sum2)
            elif sum2 > 0 and sum1 == 0 and s1[idx1].isalpha():  # number-alpha comparision
                self.dp[(idx1, idx2, sum1, sum2)] = self.possiblyEqualsUtil(s1, s2, idx1-1, idx2, sum1, sum2-1)
            elif s1[idx1].isalpha() and s2[idx2].isalpha(): # alpha-alpha comparision
                if s1[idx1]==s2[idx2]:
                    self.dp[(idx1, idx2, sum1, sum2)] = self.possiblyEqualsUtil(s1, s2, idx1-1, idx2-1, sum1, sum2)
                else:
                    self.dp[(idx1, idx2, sum1, sum2)] = False
            else:
                raise NotImplementedError
        return self.dp[(idx1, idx2, sum1, sum2)]

    def possiblyEquals(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        self.values_cache = dict()
        self.dp = dict()
        return self.possiblyEqualsUtil(s1, s2, len(s1)-1, len(s2)-1, 0, 0)
        