'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-21 09:50:32
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-21 09:52:30
FilePath: \Leetcode_Solver\1460.通过翻转子数组使两个数组相等.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1460 lang=python3
#
# [1460] 通过翻转子数组使两个数组相等
#

# @lc code=start
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        
        # if len(target) != len(arr):
        #     return False
        # else :
        #     return set(target) == set(arr) and all(target.count(i) == arr.count(i) for i in set(target))
        
        return sorted(target) == sorted(arr)
        
# @lc code=end

