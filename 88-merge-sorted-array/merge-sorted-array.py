class Solution:
   def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    if len(nums2) == 0:
            return
        
    shift = 0
    for i in range(m + n):
        try:
            if nums1[i] >= nums2[0] or (nums1[i] == 0 and i >= (m + shift)):
                nums1.insert(i, nums2[0])
                nums2.pop(0)
                nums1.pop()
                shift += 1
        except:
            return
        


        
        