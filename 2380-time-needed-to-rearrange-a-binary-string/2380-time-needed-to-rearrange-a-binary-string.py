class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        arr = list(s)
        def ret01(arr):
            vals = set()
            for i in range(len(arr)-1):
                if arr[i] == '0' and arr[i+1] == '1':
                    vals.add(i)
            return vals
        val, result = ret01(arr), 0
        while val:
            for i in val:
                arr[i], arr[i+1] = '1', '0'
            val = ret01(arr)
            result += 1
        return result
            
        