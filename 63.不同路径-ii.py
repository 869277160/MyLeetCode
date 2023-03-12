'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-15 16:18:47
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-15 21:17:56
FilePath: \Leetcode_Solver\63.不同路径-ii.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=63 lang=python3
#
# [63] 不同路径 II
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]):
    # def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
       
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        # 终点等于石头, 无语了
        if obstacleGrid[0][0] == 1:
            return 0
        else:
            # 单一路径
            if (m == 1) :
                linepath = obstacleGrid[0]
                if (1 not in linepath):
                    return 1
                else:
                    return 0
            if (n == 1):
                rowpath = [obstacleGrid[i][0] for i in range(m)]
                if (1 not in rowpath):
                    return 1
                else:
                    return 0
                
            # # # 双路径
            # if (m == 2) : 
            #     linepath = obstacleGrid[0] + obstacleGrid[1]
            #     if (1 not in rowpath):
            #         return 1
            #     else:
            #         return n + 1
            # if (n == 2):
            #     rowpath = [obstacleGrid[i][0] for i in range(m)] + [obstacleGrid[i][1] for i in range(m)]
            #     if (1 not in linepath):
            #         return 1
            #     else:
            #         return m + 1
            
            # 矩阵路径，随机放置石头
            if m > 1 and n > 1:
                res = []
                for i in range(0,m):
                    res.append([])
                    for j in range(0,n):
                        res[i].append(0)
                
                # 初始节点只有一条路径
                res[0][0] = 1
                
                # 初始化边，如果之前没有石头，就是1，否则为0
                for i in range(1,n):
                    if 1 not in obstacleGrid[0][:i+1]:
                        res[0][i] = 1
                    else:
                        res[0][i] = 0
                        
                for i in range(m):
                    if 1 not in [obstacleGrid[k][0] for k in range(i+1)]:
                        res[i][0] = 1
                    else:
                        res[i][0] = 0

                # 根据边推理中间节点
                for i in range(1,m):
                    for j in range(1,n):
                        # 障碍物没有路径
                        if obstacleGrid[i][j] == 1 :
                            res[i][j] = 0
                        # 可以走
                        if obstacleGrid[i][j] == 0 :
                            # # 边路径只有1
                            # if i == 0 :
                            #     if obstacleGrid[i][j-1] == 0:
                            #         res[i][j] = 1
                            #     if obstacleGrid[i][j-1] == 1:
                            #         res[i][j] = 0
                            # if j == 0 and i != 0:
                            #     if obstacleGrid[i-1][j] == 0:
                            #         res[i][j] = 1
                            #     if obstacleGrid[i-1][j] == 1 :
                            #         res[i][j] = 0
                            # 两个方向相加
                            if i-1 >= 0 and j-1 >= 0:
                                if obstacleGrid[i-1][j] !=1 and obstacleGrid[i][j-1] != 1:
                                    res[i][j] = res[i-1][j]+res[i][j-1]
                                if obstacleGrid[i-1][j] ==1 and  obstacleGrid[i][j-1] != 1:
                                    res[i][j] = res[i][j-1]
                                if obstacleGrid[i-1][j] !=1 and  obstacleGrid[i][j-1] == 1:
                                    res[i][j] = res[i-1][j]
                                if obstacleGrid[i-1][j] ==1 and  obstacleGrid[i][j-1] == 1:
                                    res[i][j] = 0
                            
                return res[m-1][n-1]
                # return res
    
    
# @lc code=end

