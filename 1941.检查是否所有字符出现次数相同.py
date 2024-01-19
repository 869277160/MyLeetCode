'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-16 23:34:12
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-16 23:35:53
FilePath: \Leetcode_Solver\1941.检查是否所有字符出现次数相同.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1941 lang=python3
#
# [1941] 检查是否所有字符出现次数相同
#

# @lc code=start
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        import collections
        return True if len(set(collections.Counter(s).values())) == 1 else False
# @lc code=end

