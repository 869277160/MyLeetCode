'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-27 22:00:29
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-20 14:42:26
FilePath: \Leetcode_Solver\1528.重新排列字符串.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1528 lang=python3
#
# [1528] 重新排列字符串
#

# @lc code=start
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        
        if indices == [i for i in range(len(indices))]:
            return s
        
        res = ["" for i in range(len(indices))]
        for i in range(len(indices)):
            res[indices[i]] = s[i]
        
        return "".join(res)
        
        
        
# @lc code=end

