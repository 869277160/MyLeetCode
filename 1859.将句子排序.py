'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-01 09:56:15
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-01 10:01:02
FilePath: \Leetcode_Solver\1859.将句子排序.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1859 lang=python3
#
# [1859] 将句子排序
#

# @lc code=start
class Solution:
    def sortSentence(self, s: str) -> str:
        
        words = s.split(" ")
        
        res = ["" for i in words]

        for word in words:
            res[int(word[-1])-1] = word[:-1]
        
        return " ".join(res)
        
# @lc code=end

