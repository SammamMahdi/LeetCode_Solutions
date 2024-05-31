class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        sum, a = 0, bank[0].count("1")
        for row in bank[1:]:
            n = row.count("1")
            if n != 0:
                sum += a * n
                a = n
        return sum
        
        