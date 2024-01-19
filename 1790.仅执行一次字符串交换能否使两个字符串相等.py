'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-21 10:04:23
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-21 10:12:57
FilePath: \Leetcode_Solver\1790.仅执行一次字符串交换能否使两个字符串相等.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1790 lang=python3
#
# [1790] 仅执行一次字符串交换能否使两个字符串相等
#

# @lc code=start
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        
        if len(s1) != len(s2):
            return False 
        else :
            if s1 == s2:
                return True
            else:
                for i in range(len(s1)):
                    for j in range(i+1, len(s1)):
                        # print(i,j)
                        if s2[j] == s1[i] and s2[i] == s1[j] :
                            # print(i,j)
                            # print(s1[:i], s1[i+1:j],s1[j+1:])
                            # print(s2[:i], s2[i+1:j],s2[j+1:])
                            if s1[:i] + s1[j] + s1[i+1:j] +s1[i]+ s1[j+1:] == s2:
                                return True 
                return False
        
# @lc code=end

