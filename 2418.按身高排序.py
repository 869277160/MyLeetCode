'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-21 23:37:42
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-21 23:38:41
FilePath: \Leetcode_Solver\2418.按身高排序.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2418 lang=python3
#
# [2418] 按身高排序
#

# @lc code=start
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        
        return sorted(names,key=lambda x:(-heights[names.index(x)]))
        
        
# @lc code=end

