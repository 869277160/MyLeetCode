'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-01 09:46:52
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-01 09:49:03
FilePath: \Leetcode_Solver\1539.第-k-个缺失的正整数.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1539 lang=python3
#
# [1539] 第 k 个缺失的正整数
#

# @lc code=start
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        count = 0
        for i in range(1,len(arr)+k+1):
            if i in arr:
                pass
            else :
                count += 1
            
            if count == k:
                return i
        
        
        
# @lc code=end

