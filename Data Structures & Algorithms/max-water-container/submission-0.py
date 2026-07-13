class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left=0
        right=len(heights)-1
        ans=0
        while left < right:
            width=right-left
            area=min(heights[left],heights[right])*width
            ans=max(ans,area)
            if(heights[left]<heights[right]):
                left=left+1
            else:
                right=right-1
        return ans
   
        