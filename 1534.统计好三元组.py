'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-18 15:45:00
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-18 15:46:32
FilePath: \Leetcode_Solver\1534.统计好三元组.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1534 lang=python3
#
# [1534] 统计好三元组
#

# @lc code=start
class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        
        res = 0
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if abs(arr[i]-arr[j]) <= a:
                    for k in range(j+1, len(arr)):
                        if abs(arr[j]-arr[k]) <= b and abs(arr[i]-arr[k]) <= c:
                            res += 1
            
        return res
        
# @lc code=end

