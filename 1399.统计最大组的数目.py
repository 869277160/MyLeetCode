'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-21 23:07:48
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-21 13:29:03
FilePath: \Leetcode_Solver\1399.统计最大组的数目.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1399 lang=python3
#
# [1399] 统计最大组的数目
#

# @lc code=start
class Solution:
    def countLargestGroup(self, n: int) -> int:
        res_sum = [0 for i in range(0,4*9+1)]
        
        for i in range(1,n+1):
            res_sum[sum([int(j) for j in str(i)])] +=1
        
        max_freq = max(res_sum)
        return res_sum.count(max_freq)
        
        
        
        
        
# @lc code=end

