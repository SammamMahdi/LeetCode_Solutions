class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        c = 1
        i = 0
        while i<len(nums):
            if i==0:
                curr = nums[i]
            elif nums[i] == curr:
                c+=1
                if c>2:
                    nums.pop(i)
                    continue
            else:
                curr = nums[i]
                c=1
            
            i+=1
        return len(nums)
            



            
        
            

        
    
        
        


        