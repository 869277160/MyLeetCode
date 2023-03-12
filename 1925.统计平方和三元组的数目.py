'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-21 23:02:58
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-21 23:05:53
FilePath: \Leetcode_Solver\1925.统计平方和三元组的数目.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1925 lang=python3
#
# [1925] 统计平方和三元组的数目
#

# @lc code=start
class Solution:
    def countTriples(self, n: int) -> int:
        import math 
        
        count = 0
        for i in range(1, n+1):
            for j in range(1, n+1):
                if i != j:
                    if int(math.sqrt(i**2 + j**2))**2 == (i**2 + j**2):
                        if int(math.sqrt(i**2 + j**2)) <= n:
                            count +=1 
        
        return count 
        
        
        
# @lc code=end

