class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int: 
        return self.slidingWindowAtMost(nums, k) - self.slidingWindowAtMost(nums, k - 1)

    def slidingWindowAtMost(self, nums: List[int], k: int) -> int:
        count = Counter()
        i, j = 0, 0
        res = 0
        while j < len(nums):
            count[nums[j]] += 1
            while len(count) > k:
                count[nums[i]] -= 1
                if count[nums[i]] == 0:
                    del count[nums[i]]
                i += 1
            res += j - i+1
            j += 1
        return res