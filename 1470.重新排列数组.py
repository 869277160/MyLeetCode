'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-28 09:30:28
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-28 09:31:28
FilePath: \Leetcode_Solver\1470.重新排列数组.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1470 lang=python3
#
# [1470] 重新排列数组
#

# @lc code=start
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        
        res = []
        for i in range(0,len(nums)//2):
            res.append(nums[i])
            res.append(nums[i+len(nums)//2])
        return res

         
        
        
# @lc code=end

