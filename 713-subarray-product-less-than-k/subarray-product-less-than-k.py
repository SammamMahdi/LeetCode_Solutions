class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        i = j = 0
        product = 1
        count = 0
        while j < len(nums):
            product = product * nums[j]
            if product >= k:
                while product >= k and i <= j:
                    product = product // nums[i]
                    i += 1
            count += j - i + 1
            j += 1
        return count

        