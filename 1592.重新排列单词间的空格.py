'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-21 13:55:59
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-21 13:59:18
FilePath: \Leetcode_Solver\1592.重新排列单词间的空格.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1592 lang=python3
#
# [1592] 重新排列单词间的空格
#

# @lc code=start
class Solution:
    def reorderSpaces(self, text: str) -> str:
        
        words = [word for word in text.split(" ") if word != ""]
        all_space = text.count(" ")
        
        if len(words) == 1:
            return words[0] + " "*all_space
        else :
            rest = all_space % (len(words)-1)
            space_per_word = all_space // (len(words)-1)
            return (" "*space_per_word).join(words) + " "*rest
        
        
        
        
# @lc code=end

