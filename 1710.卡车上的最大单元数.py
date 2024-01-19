'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-21 09:23:01
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-21 09:24:49
FilePath: \Leetcode_Solver\1710.卡车上的最大单元数.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1710 lang=python3
#
# [1710] 卡车上的最大单元数
#

# @lc code=start
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        boxTypes = sorted(boxTypes,key=lambda x: x[1],reverse=True)
        
        res = 0
        for i in range(len(boxTypes)):
            if truckSize >= boxTypes[i][0]:
                truckSize -= boxTypes[i][0]
                res += boxTypes[i][0] * boxTypes[i][1]
            else:
                res += truckSize * boxTypes[i][1]
                return res 
                break
        
        
        return res 
        
        
        
# @lc code=end

