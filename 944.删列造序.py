'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-20 20:02:54
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-20 20:03:34
FilePath: \Leetcode_Solver\944.删列造序.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=944 lang=python3
#
# [944] 删列造序
#

# @lc code=start
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        
        # 按照行遍历
        res = 0
        for i in range(len(strs[0])):
            for j in range(len(strs)-1):
                if strs[j][i] > strs[j+1][i]:
                    res += 1
                    break
        return res
        
        
        
# @lc code=end

