'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-19 15:35:49
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-19 15:38:16
FilePath: \Leetcode_Solver\1796.字符串中第二大的数字.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1796 lang=python3
#
# [1796] 字符串中第二大的数字
#

# @lc code=start
class Solution:
    def secondHighest(self, s: str) -> int:
        
        res = [0] * 10 
        nums = "0123456789"
        
        for i in s :
            if i in nums:
                res[int(i)] +=1 
        
        if sum(res) == 0 or sum(res) == 1:
            return -1
        
        count = 0
        
        res = res[::-1]
        for i in range(len(res)):
            if res[i] > 0:
                count += 1
            if count == 2:
                return 9-i
        
        if count == 1:
            return -1
        
        
# @lc code=end

