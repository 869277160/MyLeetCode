'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-23 09:38:49
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-23 12:51:08
FilePath: \Leetcode_Solver\2133.检查是否每一行每一列都包含全部整数.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2133 lang=python3
#
# [2133] 检查是否每一行每一列都包含全部整数
#

# @lc code=start
class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        
        check_row = all([set(matrix[i]) == set([j for j in range(1,len(matrix)+1)]) for i in range(len(matrix))])
        
        if check_row == False:
            return False 
        else :
            for j in range(0,len(matrix)):
                if set([matrix[i][j] for i in range(len(matrix))]) != set([i for i in range(1,len(matrix)+1)]):
                    return False
            return True            
        
# @lc code=end

