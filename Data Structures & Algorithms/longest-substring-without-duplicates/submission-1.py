class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen={}
        left=0
        best=0
        for i,x in enumerate(s):
            if x in seen and seen[x] >= left:
                left = seen[x]+1
            seen[x] = i
            best = max(best,i-left+1)
        return best
            

        