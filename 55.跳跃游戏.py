'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-13 10:31:38
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-13 10:37:25
FilePath: \Leetcode_Solver\55.跳跃游戏.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        if len(nums) == 1:
            return True

        
        max_pos = 0
        for i in range(0,len(nums)-1):
            max_pos = max(max_pos, i+nums[i])
            if max_pos <= i:
                return False
            
        return max_pos>=len(nums)-1

        
        
# @lc code=end

