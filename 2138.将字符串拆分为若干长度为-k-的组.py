'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-20 15:50:37
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-20 15:51:46
FilePath: \Leetcode_Solver\2138.将字符串拆分为若干长度为-k-的组.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2138 lang=python3
#
# [2138] 将字符串拆分为若干长度为 k 的组
#

# @lc code=start
class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        total_len = len(s)
        rest= total_len % k
        
        if rest == 0 :
            return [s[i:i+k] for i in range(0,total_len,k)]
        else:
            res = []
            for i in range(0,total_len-rest,k):
                res.append(s[i:i+k])
            res.append(s[-rest:]+fill*(k-rest))
            return res
        
        
        
        
# @lc code=end

