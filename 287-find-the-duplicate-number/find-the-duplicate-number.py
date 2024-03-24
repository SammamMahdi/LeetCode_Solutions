class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        set1 = set()
        for i in nums:
            if i in set1:
                return i
            set1.add(i)
        