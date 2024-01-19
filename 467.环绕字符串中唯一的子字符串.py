'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-14 09:50:12
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-14 10:22:56
FilePath: \Leetcode_Solver\467.环绕字符串中唯一的子字符串.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=467 lang=python3
#
# [467] 环绕字符串中唯一的子字符串
#

# @lc code=start
class Solution:
    def findSubstringInWraproundString(self, s: str) :
        


# def findSubstringInWraproundString(s: str) :
    
        # basestr= "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
        
        # if len(s) == 1:
        #     return 1 
        
        # if s in basestr:
        #     return len(s)*(1+len(s)) // 2
        
        # # 初始化为单一字符串
        # total = len(set([i for i in s]))
        
        # current_max = -1
        # for i in range(len(s)-2,0,-1):
        #     # return i
        #     if i > current_max:
        #         temp_set = set()
        #         for j in range(0,len(s)-i):
        #             # print(s[j:j+i+1])
        #             if s[j:j+i+1] in basestr and s[j:j+i+1] not in temp_set:
        #                 total += i*(1+i) // 2
        #                 current_max = i
        #                 temp_set.add(s[j:j+i+1])
        # return total


# @lc code=end

