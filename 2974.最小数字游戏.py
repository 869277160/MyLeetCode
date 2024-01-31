'''
Author: DingWang wangding19@mails.ucas.ac.cn
Date: 2024-01-29 16:50:26
LastEditors: DingWang wangding19@mails.ucas.ac.cn
LastEditTime: 2024-01-29 16:51:22
FilePath: \Leetcode_Solver\2974.最小数字游戏.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2974 lang=python3
#
# [2974] 最小数字游戏
#

# @lc code=start
class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = []
        for i in range(0,len(nums),2):
            res += nums[i:i+2][::-1]
            
        return res 
        
# @lc code=end

