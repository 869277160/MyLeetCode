'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-26 10:46:56
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-26 10:49:40
FilePath: \Leetcode_Solver\739.每日温度.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=739 lang=python3
#
# [739] 每日温度
#

# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = [0 for iu in temperatures]
        # stack = []
        index_stack = []
        for i in range(len(temperatures)-1,-1,-1):
            while(index_stack != [] and temperatures[index_stack[-1]] <= temperatures[i]):
                # stack.pop()
                index_stack.pop()
            res[i] = index_stack[-1] - i if index_stack != [] else 0
            # stack.append(temperatures[i])
            index_stack.append(i)
        
        return res 
        
        
        
# @lc code=end

