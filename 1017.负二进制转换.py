'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-17 16:31:39
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-17 16:38:27
FilePath: \Leetcode_Solver\1017.负二进制转换.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1017 lang=python3
#
# [1017] 负二进制转换
#

# @lc code=start
class Solution:
    def baseNeg2(self, n: int) -> str:
        # res = [0,1,110,111,100,101,1010,]
        
        N = n
        res = ''
        while N:
            N, k = -(N // 2), N % 2
            res = str(k)+res
        return res if res else '0'
# 0 0
# 1 
        
# @lc code=end

