'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-21 09:32:20
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-21 09:33:12
FilePath: \Leetcode_Solver\1725.可以形成最大正方形的矩形数目.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1725 lang=python3
#
# [1725] 可以形成最大正方形的矩形数目
#

# @lc code=start
class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        
        res = [min(r) for r in rectangles]
        
        
        return res.count(max(res))
        
        
# @lc code=end

