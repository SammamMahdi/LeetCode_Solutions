class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = Counter(nums)
        for elem,count in c.items():
            if count>len(nums)//2:
                return elem
        
        