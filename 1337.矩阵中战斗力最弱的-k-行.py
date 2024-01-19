'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-20 23:33:35
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-21 09:21:13
FilePath: \Leetcode_Solver\1337.矩阵中战斗力最弱的-k-行.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1337 lang=python3
#
# [1337] 矩阵中战斗力最弱的 K 行
#

# @lc code=start
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        
        # power = {i:sum(mat[i]) for i in range(len(mat))}
        power = [sum(mat[i]) for i in range(len(mat))]
        
        res = [i for i in range(len(mat))]
        # print(power)
        res = sorted(res,key= lambda x: (power[x],x))
        
        # print(res)
        return res[:k]
        
# @lc code=end

