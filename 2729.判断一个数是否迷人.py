'''
Author: DingWang wangding19@mails.ucas.ac.cn
Date: 2024-01-29 15:33:33
LastEditors: DingWang wangding19@mails.ucas.ac.cn
LastEditTime: 2024-01-29 15:35:19
FilePath: \Leetcode_Solver\2729.判断一个数是否迷人.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2729 lang=python3
#
# [2729] 判断一个数是否迷人
#

# @lc code=start
class Solution:
    def isFascinating(self, n: int) -> bool:
        from collections import Counter
        target = Counter("123456789")
        now = Counter(str(n)+str(2*n)+str(3*n))
        
        return True if target == now else False
        
        
# @lc code=end

