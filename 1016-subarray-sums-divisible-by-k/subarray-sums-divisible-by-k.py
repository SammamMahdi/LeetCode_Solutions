class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        count = 0
        remainder = {0: 1}
        for num in nums:
            prefix_sum += num
            mod = prefix_sum % k
            count += remainder.get(mod, 0)
            remainder[mod] = remainder.get(mod, 0) + 1
        return count
        