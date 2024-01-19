#
# @lc app=leetcode.cn id=448 lang=python3
#
# [448] 找到所有数组中消失的数字
#

# @lc code=start
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        current_sum = sum(nums)
        total_sum = sum(range(1,len(nums)+1))
        
        diff = total_sum - current_sum 
        
        
        
        
# @lc code=end

