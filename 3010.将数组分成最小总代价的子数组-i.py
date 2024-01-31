#
# @lc app=leetcode.cn id=3010 lang=python3
#
# [3010] 将数组分成最小总代价的子数组 I
#

# @lc code=start
class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        
        if len(nums) == 3:
            return sum(nums)
        
        res = sum(nums)
        for i in range(1, len(nums)-1):
            for j in range(i+1, len(nums)):
                res = min(res, nums[0] + nums[i] + nums[j])
                # print(nums[0] , nums[i] , nums[j])
        return res
        
# @lc code=end

