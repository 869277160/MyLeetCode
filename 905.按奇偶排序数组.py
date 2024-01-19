'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-20 20:24:39
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-20 20:25:43
FilePath: \Leetcode_Solver\905.按奇偶排序数组.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=905 lang=python3
#
# [905] 按奇偶排序数组
#

# @lc code=start
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        
        even = [i for i in nums if i % 2 == 0]
        odd = [i for i in nums if i % 2 != 0]
        
        return even + odd 
        
        
# @lc code=end

