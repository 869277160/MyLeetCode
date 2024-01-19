'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-18 11:49:57
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-18 11:55:03
FilePath: \Leetcode_Solver\2496.数组中字符串的最大值.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2496 lang=python3
#
# [2496] 数组中字符串的最大值
#

# @lc code=start
class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        
        uniq = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        def check(word):
            for i in word:
                if i in uniq:
                    return True
            return False

        lens = []
        for word in strs:
            if check(word) == True :
                lens.append(len(word))
            else :
                lens.append(int(word))

        return max(lens) if lens!=[] else 0
        
# @lc code=end

