class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        nums = []
        for row in bank:
            n = row.count("1")
            if n!=0:
                nums.append(n)
        sum = 0
        for i in range(len(nums)-1):
            sum+=nums[i]*nums[i+1]
        return sum
        