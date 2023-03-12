'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-21 22:42:48
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-21 22:46:38
FilePath: \Leetcode_Solver\2042.检查句子中的数字是否递增.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2042 lang=python3
#
# [2042] 检查句子中的数字是否递增
#

# @lc code=start
class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        
        items = s.split(" ")
        
        res = []
        for item in items :
            if item.isdigit():
                res.append(int(item))
        
        return res == sorted(res) and len(res) == len(set(res))
        
        
# @lc code=end

