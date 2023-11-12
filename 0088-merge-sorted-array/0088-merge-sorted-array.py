class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        result, ind1, ind2 = [], 0, 0
        
        while ind1 < m or ind2 < n:
            if ind1 == m:
                result.append(nums2[ind2])
                ind2 += 1
            elif ind2 == n:
                result.append(nums1[ind1])
                ind1 += 1
            elif nums1[ind1] >= nums2[ind2]:
                result.append(nums2[ind2])
                ind2+=1
            else:
                result.append(nums1[ind1])
                ind1 += 1
        for i in range(len(result)):
            nums1[i] = result[i]
        
    