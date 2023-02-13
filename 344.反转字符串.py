'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-13 09:37:50
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-13 09:39:52
FilePath: \Leetcode_Solver\344.反转字符串.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=344 lang=python3
#
# [344] 反转字符串
#

# @lc code=start
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s)-1
        
        while(left<right):
            temp = s[left]
            s[left] = s[right]
            s[right] = temp 
            
            left +=1 
            right -=1 
            
            
        
        
# @lc code=end

