'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-18 16:04:44
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-18 16:05:23
FilePath: \Leetcode_Solver\1346.检查整数及其两倍数是否存在.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1346 lang=python3
#
# [1346] 检查整数及其两倍数是否存在
#

# @lc code=start
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        
        for i in sorted(arr):
            if i == 0 and arr.count(i) > 1:
                return True
            if i != 0 and i*2 in arr:
                return True
        
        return False

# @lc code=end

