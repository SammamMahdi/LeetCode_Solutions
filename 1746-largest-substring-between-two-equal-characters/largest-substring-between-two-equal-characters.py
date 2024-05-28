class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        se = {}
        maxlength = -1
        for i in range(len(s)):
            if s[i] in se:
                maxlength = max(maxlength, i - se[s[i]] - 1)
            else:
                se[s[i]] = i
        return maxlength
        