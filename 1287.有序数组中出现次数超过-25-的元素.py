'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-23 12:52:06
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-23 12:53:41
FilePath: \Leetcode_Solver\1287.有序数组中出现次数超过-25-的元素.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1287 lang=python3
#
# [1287] 有序数组中出现次数超过25%的元素
#

# @lc code=start
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        
        import collections 
        freq =  collections.Counter(arr)
        res = freq.most_common(1)[0][0]
        
        return res 
        
        
        
# @lc code=end

