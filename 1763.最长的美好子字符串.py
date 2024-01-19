'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-21 10:15:45
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-04-19 22:21:32
FilePath: \Leetcode_Solver\1763.最长的美好子字符串.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1763 lang=python3
#
# [1763] 最长的美好子字符串
#

# @lc code=start
class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        
        # alphabet_lower = "abcdefghijklmnopqrstuvwxyz"
        # alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        
        # res = s[0]
        
        # # current_str = s[0]
        # # current_upper = False
        # # current_lower = False
        # # start = 0
        # # end = 0 
        # temp_res = s[0]
        
        # for i in range(1,len(s)):
        #     if (s[i] in alphabet_lower and s[i].upper() in temp_res) or (s[i] in alphabet_upper and s[i].lower() in temp_res):
        #         temp_res += s[i]
        #     else:   
        #         if len(temp_res) > len(res):
        #             res = temp_res
        #         temp_res = s[i]
        #     print(res,temp_res)
        # # if end - start > end_result - start_result:
        # #     start_result = start
        # #     end_result = end
        # if len(temp_res) > len(res):
        #     res = temp_res
            
        
        # return res if len(res)>1 else ""
        
        
        
# @lc code=end

