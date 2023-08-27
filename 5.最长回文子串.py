'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-13 10:04:00
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-13 15:47:06
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
            
        # # # # 暴力法 (不对)
        # res = ""
        # left, right = 0, len(s)
        # while(left < right):
        #     if self.checkPalindrome(s[left:right]) and len(s[left:right]) >= len(res) :
        #             res = s[left:right]
        #     if self.checkPalindrome(s[left+1:right]) and len(s[left+1:right]) >= len(res) :
        #             res = s[left+1:right]
        #     if self.checkPalindrome(s[left:right-1]) and len(s[left:right-1]) >= len(res) :
        #             res = s[left:right-1]
            
        #     left +=1
        #     right -=1 
            
       
        # left, right = 0, len(s)
        # while(left < right):
        #     if self.checkPalindrome(s[left:right]) and len(s[left:right]) >= len(res) :
        #             res = s[left:right]
        #     if self.checkPalindrome(s[left+1:right]) and len(s[left+1:right]) >= len(res) :
        #             res = s[left+1:right]
        #     if self.checkPalindrome(s[left:right-1]) and len(s[left:right-1]) >= len(res) :
        #             res = s[left:right-1]
            
        #     left +=1

        # left, right = 0, len(s)
        # while(left < right):
        #     if self.checkPalindrome(s[left:right]) and len(s[left:right]) >= len(res) :
        #             res = s[left:right]
        #     if self.checkPalindrome(s[left+1:right]) and len(s[left+1:right]) >= len(res) :
        #             res = s[left+1:right]
        #     if self.checkPalindrome(s[left:right-1]) and len(s[left:right-1]) >= len(res) :
        #             res = s[left:right-1]
            
        #     right -=1 
        
        #中心扩散法
        start, end = 0, 0
        for i in range(0,len(s)):
            len1 = self.expandAroundCenter(s, i, i)
            len2 = self.expandAroundCenter(s, i, i+1)
            max_len = max(len1, len2)
            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2

        return s[start:end + 1];

    
    def expandAroundCenter(self,s: str,left, right):
        L, R = left, right
        while (L >= 0 and R < len(s) and s[L] == s[R]):
                L -= 1
                R += 1

        return R - L - 1;
        
# @lc code=end

