'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-27 11:56:15
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-20 23:28:10
FilePath: \Leetcode_Solver\1331.数组序号转换.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1331 lang=python3
#
# [1331] 数组序号转换
#

# @lc code=start
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        
        # arr_index = sorted(set(arr))
        # res = [0 for i in arr]
        # for i in range(len(arr)):
        #     res[i] = arr_index.index(arr[i])+1
        
        # return res 
        
        a = sorted(set(arr))
        d = {}
        for i, v in enumerate(a, 1):
            d[v] = i
        return [d[i] for i in arr]
        
        
        
# @lc code=end

