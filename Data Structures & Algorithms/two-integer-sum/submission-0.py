class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        see={}
        for i,x in enumerate(nums):
            want=target-x     
            if want in see:
                return [see[want],i]
            see[x]=i
        return [] 