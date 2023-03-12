'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-21 23:11:46
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-21 23:15:40
FilePath: \Leetcode_Solver\1089.复写零.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1089 lang=python3
#
# [1089] 复写零
#

# @lc code=start
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        if 0 not in arr or sum(arr) == 0:
            return 
        else :
            i=0
            while i < len(arr)-1:
                if arr[i] == 0:
                    arr[i+2:]=arr[i+1:-1]
                    arr[i+1] = 0
                    i +=1
                i +=1 
            return 

# @lc code=end

