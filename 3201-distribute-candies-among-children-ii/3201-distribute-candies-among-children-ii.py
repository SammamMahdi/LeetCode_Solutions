class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        m = min(n, limit)
        count = 0
        for i in range(m + 1):
            count += max(min(limit, n - i) - max(0, n - i - limit) + 1, 0)
        return count
        