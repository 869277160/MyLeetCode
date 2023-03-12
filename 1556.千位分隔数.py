'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-18 15:52:24
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-18 15:55:02
FilePath: \Leetcode_Solver\1556.千位分隔数.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1556 lang=python3
#
# [1556] 千位分隔数
#

# @lc code=start
class Solution:
    def thousandSeparator(self, n: int) -> str:
        
        strs = str(n)
        if len(strs) <= 3:
            return strs
        else :
            strs = strs[::-1]
            res = ""
            for i in range(len(strs)):
                if i % 3 == 0 and i != 0:
                    res+="."
                res += (strs[i])
            
            
        return res[::-1]
# @lc code=end

