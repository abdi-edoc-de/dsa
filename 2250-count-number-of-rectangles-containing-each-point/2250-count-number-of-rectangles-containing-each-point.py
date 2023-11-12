class Solution(object):
    def countRectangles(self, rectangles, points):
        """
        :type rectangles: List[List[int]]
        :type points: List[List[int]]
        :rtype: List[int]
        """
        count = defaultdict(list)
        for l, h in rectangles:
            for valh in range(1, h + 1):
                count[valh].append(l)
        for k, v in count.items():
            v.sort()
        def binarySearch(arr, target):
            r, l, best = len(arr)-1, 0, -1
            while l<=r:
                mid = l+((r-l)//2)
                if target <= arr[mid]:
                    best = mid
                    r = mid - 1
                else: 
                    l = mid + 1
                
            return best 
        result = []
        for x, y in points:
            best = binarySearch(count[y], x)
            if best == -1:
                result.append(0)
            else:
                result.append(len(count[y])- (best))
        
        return result
