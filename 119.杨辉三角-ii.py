'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-13 10:55:22
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-13 11:08:48
FilePath: \Leetcode_Solver\119.杨辉三角-ii.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=119 lang=python3
#
# [119] 杨辉三角 II
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        if rowIndex == 0 : return [1]
        if rowIndex == 1 : return [1,1]
        if rowIndex == 2 : return [1,2,1]
        if rowIndex == 3 : return [1,3,3,1]
        if rowIndex > 3:
            temp = self.getRow(rowIndex-1)
            res = [1]
            for i in range(1,rowIndex):
                res.append(temp[i-1]+temp[i])
            res.append(1);
        
        return res 
        
# @lc code=end

