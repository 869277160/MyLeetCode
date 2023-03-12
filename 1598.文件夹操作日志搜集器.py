'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-05 16:28:06
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-05 16:31:04
FilePath: \Leetcode_Solverd:\Leetcode_Solver\1598.文件夹操作日志搜集器.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1598 lang=python3
#
# [1598] 文件夹操作日志搜集器
#

# @lc code=start
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        
        current_depth = 0 
        
        for log in logs:
            if log == "../":
                current_depth = max(0,current_depth-1)
            elif log == "./":
                current_depth = current_depth
            else :
                current_depth +=1 
        
        return current_depth
# @lc code=end

