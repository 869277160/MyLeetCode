'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-05 12:40:30
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-05 12:41:55
FilePath: \Leetcode_Solverd:\Leetcode_Solver\2129.将标题首字母大写.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2129 lang=python3
#
# [2129] 将标题首字母大写
#

# @lc code=start
class Solution:
    def capitalizeTitle(self, title: str) -> str:
        words = title.split(" ")
        
        res = ""
        for word in words :
            if len(word) <= 2 :
                res += word.lower()
            else:
                res += word.capitalize()
            res += " "
            
        return res[:-1]
        
# @lc code=end

