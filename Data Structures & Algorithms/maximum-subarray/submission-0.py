class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub=nums[0]
        CurSum=0
        for n in nums:
            if CurSum<0:
                CurSum=0
            CurSum+=n
            maxSub=max(maxSub,CurSum)
        return maxSub
        