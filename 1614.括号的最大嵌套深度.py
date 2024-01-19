'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-20 15:04:29
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-20 15:01:09
FilePath: \Leetcode_Solver\1614.括号的最大嵌套深度.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1614 lang=python3
#
# [1614] 括号的最大嵌套深度
#

# @lc code=start
class Solution:
    def maxDepth(self, s: str) -> int:
        
        current_depth = 0
        all_depth = []
        
        for i in range (len(s)):
            if s[i] == "(":
                current_depth += 1
            elif s[i] == ")":
                current_depth -= 1
            all_depth.append(current_depth)

        return max(all_depth)
        
        
# @lc code=end

