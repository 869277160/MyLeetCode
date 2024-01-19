'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-04-07 17:22:51
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-04-07 17:25:20
FilePath: \Leetcode_Solver\973.最接近原点的-k-个点.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=973 lang=python3
#
# [973] 最接近原点的 K 个点
#

# @lc code=start
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        points.sort(key=lambda x: (x[0]**2 + x[1]**2))
        
        
        return points[:k]
        
        
        
        
# @lc code=end

