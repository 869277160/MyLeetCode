'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-18 11:34:25
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-18 11:43:10
FilePath: \Leetcode_Solver\997.找到小镇的法官.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=997 lang=python3
#
# [997] 找到小镇的法官
#

# @lc code=start
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        Judge_metrix = []
        for i in range(n):
            Judge_metrix.append([])
            for j in range(n):
                Judge_metrix[i].append(0)
            
        for item in trust:
            Judge_metrix[item[0]-1][item[1]-1] = 1
        
        for user in range(n):
            user_line = [Judge_metrix[i][user] for i in range(n)]
            user_row = Judge_metrix[user]
            
            if sum(user_line) == n-1 and sum(user_row) == 0:
                return user +1 
        
        return -1 
            
            # if sum(user) == 0:
            #     return Judge_metrix.index(user)+1
        
# @lc code=end

