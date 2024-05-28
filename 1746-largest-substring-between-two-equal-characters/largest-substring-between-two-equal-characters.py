class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        se = defaultdict(list)
        maxlength = -1
        for i in range(len(s)):
            se[s[i]].append(i)

        for i in se:
            if len(se[i]) > 1:
                maxlength = max(maxlength, se[i][-1] - se[i][0] - 1)

        return maxlength
        