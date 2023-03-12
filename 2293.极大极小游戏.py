'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-21 10:11:25
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-21 10:14:06
FilePath: \Leetcode_Solver\2293.极大极小游戏.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2293 lang=python3
#
# [2293] 极大极小游戏
#

# @lc code=start
class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        while len(nums) > 1:
            Newnums = []
            for i in range(0,len(nums),2):
                if (i//2) % 2 == 0:
                    Newnums += [min(nums[i],nums[i+1])]
                else :
                    Newnums += [max(nums[i],nums[i+1])]
            
            nums = Newnums
            
        return nums[0]
# @lc code=end

