class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        count  = Counter(nums)
        num = []
        for i in count:
            if count[i]==1:
                num.append(i)
        return num
        