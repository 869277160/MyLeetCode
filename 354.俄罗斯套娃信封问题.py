'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-24 11:39:06
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-24 11:43:55
FilePath: \Leetcode_Solver\354.俄罗斯套娃信封问题.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=354 lang=python3
#
# [354] 俄罗斯套娃信封问题
#

# @lc code=start
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        
        envelopes = sorted(envelopes, key=lambda x: (x[0], -x[1]))
        
        height_list = [x[1] for x in envelopes]
        
        res = [1 for _ in range(len(height_list))]
        
        for i in range(len(res)):
            for j in range(i):
                if height_list[i] > height_list[j]:
                    res[i] = max(res[i], res[j]+1)
        
        return max(res)
        
        
        
# @lc code=end

