class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        countnum = {}

        for i in range(len(nums)):
            countnum[nums[i]] = 1 + countnum.get(nums[i],0)

        
        for s in countnum:
            if countnum[s] >= 2:
                return True
        
        return False


