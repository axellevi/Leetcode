class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            index = haystack.find(needle)
            return index
        return -1
        