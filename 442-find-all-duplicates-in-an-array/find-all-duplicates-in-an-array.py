class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicates = set()
        set1 = set()
        for i in nums:
            if i in set1:
                duplicates.add(i)
                continue
            set1.add(i)
        return list(duplicates)
        