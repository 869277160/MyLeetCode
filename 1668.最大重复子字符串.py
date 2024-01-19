'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-20 15:09:44
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-20 15:10:50
FilePath: \Leetcode_Solver\1668.最大重复子字符串.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1668 lang=python3
#
# [1668] 最大重复子字符串
#

# @lc code=start
class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        if word not in sequence:
            return 0
        else :
            for i in range(2,(len(sequence)//len(word))+1):
                if word*i not in sequence:
                    return i-1
                
            return (len(sequence)//len(word))
# @lc code=end

