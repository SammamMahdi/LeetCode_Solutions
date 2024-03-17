class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        numsd = {}
        k = 0
        for i in range(len(nums)):
            if nums[i] not in numsd.values():
                numsd[k] = nums[i]
                k += 1
        for i in range(len(nums)):
            if i > k - 1:
                nums[i] = 0
            else:
                nums[i] = numsd[i]
        return k
        