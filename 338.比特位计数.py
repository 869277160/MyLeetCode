'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-13 17:56:59
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-13 18:06:18
FilePath: \Leetcode_Solver\338.比特位计数.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=338 lang=python3
#
# [338] 比特位计数
#

# @lc code=start
class Solution:
    def countBits(self, n: int) -> List[int]:
        
        res = [0] * (n+1)
        for i in range(1,n+1):
            # res[i] = res[i & (i-1)] + 1
        return res 
    
        # 1024 10
        # 2048 11
        # 4096 12
        # 8192 13
        # 16384 14
        
        # for i in range(0,n+1):
        #     print(bin(i).count('1'))
        
        #0,1,1,2,  1,2,3,  1,2,2,3,2,3,3,4
        #1,2,3,4,  5,6,7,  8,9,10,11,12,13,14,15,16
# @lc code=end

