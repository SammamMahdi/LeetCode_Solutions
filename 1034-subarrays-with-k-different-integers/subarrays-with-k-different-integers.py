class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int: 
        # return self.slidingWindowAtMost(nums, k) - self.slidingWindowAtMost(nums, k - 1)
        count = [0] * (len(nums) + 1)
        out, l, m = 0, 0, 0

        for x in nums:
            count[x] += 1
            if count[x] == 1:
                k -= 1
                # when degree is reached, move m away
                if k < 0:
                    count[nums[m]] = 0
                    m += 1
                    l = m
            if k <= 0:
                while count[nums[m]] > 1:
                    count[nums[m]] -= 1
                    m += 1
                out += m-l+1
        
        return out

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