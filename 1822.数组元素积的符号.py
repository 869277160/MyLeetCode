'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-19 15:40:53
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-19 15:41:43
FilePath: \Leetcode_Solver\1822.数组元素积的符号.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1822 lang=python3
#
# [1822] 数组元素积的符号
#

# @lc code=start
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        if 0 in nums :
            return 0
    
        count = 0
        for i in nums:
            if i < 0:
                count += 1
        
        return -1 if count % 2 == 1 else 1
# @lc code=end

