'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-01 09:51:56
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-01 09:53:09
FilePath: \Leetcode_Solver\1704.判断字符串的两半是否相似.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1704 lang=python3
#
# [1704] 判断字符串的两半是否相似
#

# @lc code=start
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        
        first = s[:len(s)//2]
        second = s[len(s)//2:]
        
        first_count = 0
        second_count = 0
        
        for i in first:
            if i in 'aeiouAEIOU':
                first_count += 1
        
        for i in second:
            if i in 'aeiouAEIOU':
                second_count += 1
        
        return first_count == second_count


        
        
        
        
        
        
# @lc code=end

