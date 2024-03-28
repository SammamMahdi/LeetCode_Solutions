class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        maxm = 0
        count = 0
        i, j = 0, 0
        freq = defaultdict(int)
        while j < len(nums):
            freq[nums[j]] += 1
            if freq[nums[j]] > k:
                maxm = max(maxm, j - i)
                while freq[nums[j]] > k:
                    freq[nums[i]] -= 1
                    i += 1
            j += 1
        maxm = max(maxm, j - i)
        return maxm