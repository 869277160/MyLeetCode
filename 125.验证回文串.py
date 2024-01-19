'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-15 16:25:47
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-15 17:19:53
FilePath: \Leetcode_Solver\125.验证回文串.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#

# @lc code=start
class Solution:
    # def isPalindrome(self, s: str) -> bool:
    def isPalindrome(self, s: str):
        
        # s = ''.join(filter(str.isalnum,s)).lower()
        
        uniqueelem = "qwertyuiopasdfghjklmnbvcxz1234567890"
        
        s = s.lower()
        s_replaced = ""
        for i in s:
            if i in uniqueelem:
                s_replaced += i 
            # if ord('a') <= ord(i) and ord(i) <= ord('z'):
            #     s_replaced += i
            # if ord('A') <= ord(i) and ord(i) <= ord('Z'):
            #     s_replaced += i.lower()
            # if ord('0') <= ord(i) and ord(i) <= ord('9'):
            #     s_replaced += i 
                
        # return s_replaced
        return s_replaced == s_replaced[::-1]
# @lc code=end

