class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = heights.copy()
        expected.sort()
        c = 0
        for i in range(len(expected)):
            if expected[i]!=heights[i]:
                c+=1
        return c
        