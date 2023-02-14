class Solution:
    def sumZero(self, n: int) -> List[int]:
        arr = []
        if n % 2 == 1:
            arr.append(0)
            n -=1
        for i in range(0,n,2):
            arr.append(i+1)
            arr.append(-(i+1))
        return arr