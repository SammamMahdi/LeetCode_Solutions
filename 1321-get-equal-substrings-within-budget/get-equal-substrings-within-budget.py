class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        maxlength,cost, i, j = 0, 0,0,0
        while j < len(s):
            cost += abs(ord(s[j]) - ord(t[j]))
            while cost > maxCost:
                cost -= abs(ord(s[i]) - ord(t[i]))
                i += 1
            j += 1
            maxlength = max(maxlength, j - i)

        return maxlength
        