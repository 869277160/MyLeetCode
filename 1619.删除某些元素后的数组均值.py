'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-07 18:01:20
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-07 18:02:16
FilePath: \Leetcode_Solver\1619.删除某些元素后的数组均值.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1619 lang=python3
#
# [1619] 删除某些元素后的数组均值
#

# @lc code=start
class Solution:
    def trimMean(self, arr: List[int]) -> float:
        
        res = sorted(arr)
        
        return sum(res[len(arr)//20:-len(arr)//20])/(len(arr)-len(arr)//10)
        
# @lc code=end

