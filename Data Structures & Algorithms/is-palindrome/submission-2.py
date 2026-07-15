import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        d=""
        for i in s.lower():
            if i.isalnum():
                d +=i
            print(d)
        if d == d[::-1]:
                return True
        return False
        

   
        


        