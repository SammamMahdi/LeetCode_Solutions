class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        res = 0
        min_pos = max_pos = -1
        left = -1

        for i, num in enumerate(nums):
            if num < minK or num > maxK:
                left = i
            if num == minK:
                min_pos = i
            if num == maxK:
                max_pos = i
            res += max(0, min(min_pos, max_pos) - left)

        return res
        