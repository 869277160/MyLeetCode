'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-16 22:51:33
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-16 22:52:21
FilePath: \Leetcode_Solver\771.宝石与石头.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=771 lang=python3
#
# [771] 宝石与石头
#

# @lc code=start
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        res = 0
        for i in stones:
            if i in jewels:
                res+=1 
        return res 
        
        
        
# @lc code=end

