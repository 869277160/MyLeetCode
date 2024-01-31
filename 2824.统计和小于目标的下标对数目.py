#
# @lc app=leetcode.cn id=2824 lang=python3
#
# [2824] 统计和小于目标的下标对数目
#

# @lc code=start
class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        res = 0
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] < target:
                    res += 1
        return res 
        
        
# @lc code=end

