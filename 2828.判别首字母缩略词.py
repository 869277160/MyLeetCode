'''
Author: DingWang wangding19@mails.ucas.ac.cn
Date: 2024-01-29 15:51:50
LastEditors: DingWang wangding19@mails.ucas.ac.cn
LastEditTime: 2024-01-29 15:52:38
FilePath: \Leetcode_Solver\2828.判别首字母缩略词.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2828 lang=python3
#
# [2828] 判别首字母缩略词
#

# @lc code=start
class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        target = [word[0] for word in words]
        return True if "".join(target) == s else False
        
# @lc code=end

