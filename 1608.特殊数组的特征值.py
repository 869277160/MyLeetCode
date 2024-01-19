'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-06 15:02:23
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-06 15:04:53
FilePath: \Leetcode_Solverd:\Leetcode_Solver\1608.特殊数组的特征值.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1608 lang=python3
#
# [1608] 特殊数组的特征值
#

# @lc code=start
class Solution:
    def specialArray(self, nums: List[int]) -> int:

        for i in range(len(nums)+1):
            counter = [1 for j in nums if j >= i ]
            if sum(counter) == i :
                return i 
            
        return -1 
            
        
        
# @lc code=end

