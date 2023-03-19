class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum % 2 == 1: return []
        even , result = 2, []
        while even <= finalSum:
            result.append(even)
            even , finalSum = even + 2, finalSum - even
        result[-1] += finalSum
        return result
        
        