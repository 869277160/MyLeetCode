'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-06 09:50:08
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-06 09:50:55
FilePath: \Leetcode_Solverd:\Leetcode_Solver\2154.将找到的值乘以-2.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2154 lang=python3
#
# [2154] 将找到的值乘以 2
#

# @lc code=start
class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        
        if original not in nums:
            return original
        
        else :
            while original in nums:
                original *= 2
            return original
        
        
# @lc code=end

