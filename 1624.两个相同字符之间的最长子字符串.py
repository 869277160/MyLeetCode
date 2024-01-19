'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-20 15:02:09
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-20 15:04:44
FilePath: \Leetcode_Solver\1624.两个相同字符之间的最长子字符串.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1624 lang=python3
#
# [1624] 两个相同字符之间的最长子字符串
#

# @lc code=start
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        
        all_letters = set(s)
        
        if len(all_letters) == len(s):
            return -1
        else:
            res = 0
            for i in all_letters:
                res = max(res,s.rfind(i)-s.find(i)-1)
            return res
            
        
        
        
# @lc code=end

