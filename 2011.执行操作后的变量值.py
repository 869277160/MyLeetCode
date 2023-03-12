'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-20 14:29:08
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-20 14:29:33
FilePath: \Leetcode_Solver\2011.执行操作后的变量值.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2011 lang=python3
#
# [2011] 执行操作后的变量值
#

# @lc code=start
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        res = 0
        
        for i in operations:
            if i[1] == '+':
                res += 1
            else:
                res -= 1
            
        return res
        
        
# @lc code=end

