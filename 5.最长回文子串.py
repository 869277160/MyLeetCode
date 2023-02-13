'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-13 10:04:00
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-13 10:22:12
FilePath: \Leetcode_Solver\5.最长回文子串.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        
    #     # if self.checkPalindrome(s):
    #     #     return s
        res = ""
        left, right = 0, len(s)
        while(left < right):
            if self.checkPalindrome(s[left:right]) and len(s[left:right]) >= len(res) :
                    res = s[left:right]
            if self.checkPalindrome(s[left+1:right]) and len(s[left+1:right]) >= len(res) :
                    res = s[left+1:right]
            if self.checkPalindrome(s[left:right-1]) and len(s[left:right-1]) >= len(res) :
                    res = s[left:right-1]
            
            left +=1
            right -=1 
            
       
        left, right = 0, len(s)
        while(left < right):
            if self.checkPalindrome(s[left:right]) and len(s[left:right]) >= len(res) :
                    res = s[left:right]
            if self.checkPalindrome(s[left+1:right]) and len(s[left+1:right]) >= len(res) :
                    res = s[left+1:right]
            if self.checkPalindrome(s[left:right-1]) and len(s[left:right-1]) >= len(res) :
                    res = s[left:right-1]
            
            left +=1

        left, right = 0, len(s)
        while(left < right):
            if self.checkPalindrome(s[left:right]) and len(s[left:right]) >= len(res) :
                    res = s[left:right]
            if self.checkPalindrome(s[left+1:right]) and len(s[left+1:right]) >= len(res) :
                    res = s[left+1:right]
            if self.checkPalindrome(s[left:right-1]) and len(s[left:right-1]) >= len(res) :
                    res = s[left:right-1]
            
            right -=1 
            
        
        return res 
    
    def checkPalindrome(self,input: str):
        return input == input[::-1]
        
# @lc code=end

