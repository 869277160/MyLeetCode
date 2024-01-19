'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-04-14 16:42:36
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-04-14 16:51:45
FilePath: \Leetcode_Solver\1513.仅含-1-的子串数.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1513 lang=python3
#
# [1513] 仅含 1 的子串数
#

# @lc code=start
class Solution:
    def numSub(self, s: str) -> int:
        sequencial_1 = s.split('0')

        sequencial_1_len = [len(i) for i in sequencial_1]
        
        # print(sequencial_1_len)
        
        res_lookup = [(i * (i+1) // 2 ) % (1e9 + 7 ) for i in range(max(sequencial_1_len)+1)]
        
        # print(res_lookup)
        res = [res_lookup[i] for i in(sequencial_1_len)]
    
        # print(res)
        output = int(sum(res) % (1e9 + 7 ) )
        return output
        
        
        
        
        
# @lc code=end

