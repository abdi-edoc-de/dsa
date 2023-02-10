class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        left = 0
        right = 0
        final = []
        while left < len(nums1) and right < len(nums2):
            if nums1[left] < nums2[right]:
                final.append(nums1[left])
                left += 1
            else:
                final.append(nums2[right])
                right += 1
        
        if left < len(nums1):
            while left < len(nums1):
                final.append(nums1[left])
                left += 1
        if right < len(nums2):
            while right < len(nums2):
                final.append(nums2[right])
                right += 1
        if len(final) % 2 == 0:
            median = (final[len(final)//2] + final[(len(final)//2) - 1]) / 2
        else:
            median = final[(len(final)//2)]
            
        return median