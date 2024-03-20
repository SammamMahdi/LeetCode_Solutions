class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        hash_table = {}
        start_index = -1
        for index, string in enumerate(s):
            if string in hash_table and hash_table[string] >=      start_index:
                start_index = hash_table[string]
            max_length = max(max_length, index - start_index)
            hash_table[string] = index
        return max_length