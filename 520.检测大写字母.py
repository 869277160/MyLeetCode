'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-16 22:13:19
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-16 22:18:00
FilePath: \Leetcode_Solver\520.检测大写字母.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=520 lang=python3
#
# [520] 检测大写字母
#

# @lc code=start
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) == 0 :
            return True
        
        if len(word) == 1 :
            return True

        all = []
        for w in word:
            if ord(w) <= ord('Z') and ord(w) >= ord('A'):
                all.append(1)
            else:
                all.append(0) 
        total = sum(all)
        
        
        if total == len(word) or (total == 1 and all[0] == 1) or total == 0:
            return True
        else :
            return False 
            
        
        
# @lc code=end

