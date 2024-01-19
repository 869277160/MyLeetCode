'''
Author: your name
Date: 2021-09-23 14:48:15
LastEditTime: 2021-09-23 14:54:01
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \undefinedd:\leetcode_solve\215.数组中的第k个最大元素.py
'''
#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#

# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        # return nums = sorted(nums, reverse=True)[k-1]
        
        return heapq.nlargest(k, nums)[-1]
        # return nums

        

# @lc code=end

