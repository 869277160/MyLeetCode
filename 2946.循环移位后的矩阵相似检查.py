'''
Author: DingWang wangding19@mails.ucas.ac.cn
Date: 2024-01-29 17:37:59
LastEditors: DingWang wangding19@mails.ucas.ac.cn
LastEditTime: 2024-01-29 17:52:34
FilePath: \Leetcode_Solver\2946.循环移位后的矩阵相似检查.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2946 lang=python3
#
# [2946] 循环移位后的矩阵相似检查
#

# @lc code=start
class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:

        for i in range(len(mat)):
            k = k % len(mat[i])
            if i % 2 == 0:
                if mat[i] != mat[i][k:] + mat[i][:k]:
                    return False
            else:
                if mat[i] != mat[i][-k:] + mat[i][:-k]:
                    return False
        return  True
        
        
        
# @lc code=end

