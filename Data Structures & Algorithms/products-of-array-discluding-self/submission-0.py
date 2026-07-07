class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[1]*len(nums)
        
        for i in range(len(nums)):
            
            for k in range(len(nums)):
                if i!=k:
                    
                    res[i]*=nums[k]
        return res


  



        