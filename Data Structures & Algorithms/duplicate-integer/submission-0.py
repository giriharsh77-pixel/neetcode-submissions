class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        boolean = False
        s=set()

        for num in nums:
            if num not in s:
                s.add(num)
            else:
                boolean=True

        return boolean


        

        