'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-13 14:28:45
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-04-06 17:26:32
FilePath: \Leetcode_Solver\56.合并区间.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x:x[0])
        res = [intervals[0]]
        intervals.pop(0)
        
        for next in intervals:
            current = res[-1]
            
            # 如果下一区间的起始点落在当前区间内，则更新当前区间的结束点。 
            if next[0] <= current[1]:
                current[1] = max(current[1], next[1])
            # 否则，将当前区间加入结果数组。 计算新的起始点。 
            else :
                res.append(next)
        
        return res
        
        
# @lc code=end

