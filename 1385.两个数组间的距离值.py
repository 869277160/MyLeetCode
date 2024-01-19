'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-21 13:17:05
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-21 13:17:52
FilePath: \Leetcode_Solver\1385.两个数组间的距离值.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1385 lang=python3
#
# [1385] 两个数组间的距离值
#

# @lc code=start
class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        
        count = 0
        for num in arr1:
            if all([abs(num - i) > d for i in arr2]):
                count += 1
        
        return count 
        
        
        
# @lc code=end

