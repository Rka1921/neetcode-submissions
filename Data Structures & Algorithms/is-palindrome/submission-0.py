import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        res=re.sub(r'[^a-zA-Z0-9]','',s)
        r=res.lower()
        if r == r[::-1]:
            return True
        else:
            return False
        