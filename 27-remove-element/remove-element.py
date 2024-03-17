class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        c = 0
        while c<len(nums):
            if nums[c]==val:
                nums.pop(c)
            else:
                c+=1
        return(len(nums))
            

        