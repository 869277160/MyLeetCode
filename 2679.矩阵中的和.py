#
# @lc app=leetcode.cn id=2679 lang=python3
#
# [2679] 矩阵中的和
#

# @lc code=start
class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        for row in nums:
            row.sort()
            
        res = 0
        for col in range(len(nums[0])):
            res += max([nums[row][col] for row in range(len(nums))])
        
        return res 
        
# @lc code=end

