'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-17 09:51:21
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-17 09:53:58
FilePath: \Leetcode_Solver\2427.公因子的数目.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2427 lang=python3
#
# [2427] 公因子的数目
#

# @lc code=start
class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        set1 = set()
        set2 = set()
        set1.add(1)
        set2.add(1)
        set1.add(a)
        set2.add(b)
        
        import math
        for i in range(1,max(int(math.sqrt(a)),int(math.sqrt(b)))+1):
            if a % i == 0:
                set1.add(i)
                set1.add(a//i)
            if b % i == 0:
                set2.add(i)
                set2.add(b//i)
        
        return len(set1 & set2)
                
        
        
# @lc code=end

