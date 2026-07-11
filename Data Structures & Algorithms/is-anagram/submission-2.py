class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = len(s) == len(t) and sorted(s) == sorted(t)
        return s
        