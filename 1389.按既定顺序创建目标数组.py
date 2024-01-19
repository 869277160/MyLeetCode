'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-21 13:22:49
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-21 13:25:59
FilePath: \Leetcode_Solver\1389.按既定顺序创建目标数组.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1389 lang=python3
#
# [1389] 按既定顺序创建目标数组
#

# @lc code=start
class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        
        
        res = []
        for i in range(0,len(nums)):
            if index[i] >= len(res):
                res.append(nums[i])
            else:            
                res.insert(index[i],nums[i])
        
        return res 
        
        
        
        
        
# @lc code=end

