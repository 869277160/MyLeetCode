#
# @lc app=leetcode.cn id=896 lang=python3
#
# [896] 单调数列
#

# @lc code=start
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        
        if len(nums) < 3:
            return True
        else:
            res = 0 
            for i in range(1,len(nums)):
                if nums[i] - nums[i-1] > 0:
                    if res < 0 : return False
                    else :
                        res +=1 
                if nums[i] - nums[i-1] < 0:
                    if res > 0 : return False
                    else :
                        res -=1 
                if nums[i] - nums[i-1] == 0:
                    pass
        
        return True

        
        # for i in nums:
        #     if (i <= max(nums[:i]) and i >= min(nums[:i])) or (i <= max(nums[:i]) and i >= min(nums[:i])) :
        #         return False 
        
        # return True

# @lc code=end

