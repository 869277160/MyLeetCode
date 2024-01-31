#
# @lc app=leetcode.cn id=2784 lang=python3
#
# [2784] 检查数组是否是好的
#

# @lc code=start
class Solution:
    def isGood(self, nums: List[int]) -> bool:
        
        target = [i for i in range(1,max(nums)+1)] + [max(nums)]
        # nums.sort()
        # return True if target == nums else False
        
        from collections import Counter
        return True if Counter(target) == Counter(nums) else False
        
# @lc code=end

