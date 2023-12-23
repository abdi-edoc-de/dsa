from bisect import bisect_left, bisect_right

class Solution:
    def get_start(self, nums, people):
        low, high, start = 0, len(nums) - 1, -1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] <= people:
                start = mid
                low = mid + 1
            else:
                high = mid - 1
        return start + 1

    def get_end(self, nums, people):
        low, high, end = 0, len(nums) - 1, -1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] < people:
                end = mid
                low = mid + 1
            else:
                high = mid - 1
        return end + 1

    def fullBloomFlowers(self, flowers, people):
        start_times = sorted([flower[0] for flower in flowers])
        end_times = sorted([flower[1] for flower in flowers])

        ans = []
        for time in people:
            starts = bisect_right(start_times, time)
            ends = bisect_left(end_times, time)
            ans.append(starts - ends)
        return ans


