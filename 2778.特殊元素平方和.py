#
# @lc app=leetcode.cn id=2778 lang=python3
#
# [2778] 特殊元素平方和
#

# @lc code=start
class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        
        res = 0
        for i in range(len(nums)):
            if len(nums) % (i+1) == 0:
                res += nums[i]**2
        return res 
        
# @lc code=end

