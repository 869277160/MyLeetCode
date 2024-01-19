'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-27 11:57:41
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-27 11:59:54
FilePath: \Leetcode_Solver\1436.旅行终点站.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1436 lang=python3
#
# [1436] 旅行终点站
#

# @lc code=start
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        # start = 
        # end = set(p)
        
        return (set([path[1] for path in paths]) - set([path[0] for path in paths])).pop()
        
# @lc code=end

