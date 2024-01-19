'''
Author: your name
Date: 2021-09-23 17:25:15
LastEditTime: 2021-09-23 17:26:36
LastEditors: your name
Description: In User Settings Edit
FilePath: \undefinedd:\leetcode_solve\69.x-的平方根.py
'''
#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:

        for i in range(0,2**30+1):
            if i * i > x:
                return i-1

# @lc code=end

