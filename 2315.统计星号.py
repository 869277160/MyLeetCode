'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-20 14:32:15
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-20 14:33:56
FilePath: \Leetcode_Solver\2315.统计星号.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2315 lang=python3
#
# [2315] 统计星号
#

# @lc code=start
class Solution:
    def countAsterisks(self, s: str) -> int:
        
        items = s.split("|")
        
        count = 0
        for i in range(0,len(items),2):
            for j in items[i]:
                if j == "*":
                    count += 1
            
       
        
        return count 
        
# @lc code=end

