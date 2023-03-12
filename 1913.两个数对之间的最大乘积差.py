#
# @lc app=leetcode.cn id=1913 lang=python3
#
# [1913] 两个数对之间的最大乘积差
#

# @lc code=start
class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        
        nums_sorted = sorted(nums)
        
        return (nums_sorted[-1]*nums_sorted[-2])-(nums_sorted[0]*nums_sorted[1])
        
        
# @lc code=end

