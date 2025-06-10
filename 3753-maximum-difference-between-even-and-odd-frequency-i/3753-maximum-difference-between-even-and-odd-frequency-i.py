from collections import Counter

class Solution:
    def maxDifference(self, s: str) -> int:
        count = Counter(s)
        print(count)
        max_odd = float("-inf")
        min_even = float("inf")
        for key, value in count.items():
            if value % 2 == 1:
                max_odd = max(max_odd, value)
            else:
                min_even = min(min_even, value)
        return max_odd - min_even
        