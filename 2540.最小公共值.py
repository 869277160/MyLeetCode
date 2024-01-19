'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-21 11:18:58
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-21 11:20:41
FilePath: \Leetcode_Solver\2540.最小公共值.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2540 lang=python3
#
# [2540] 最小公共值
#

# @lc code=start
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        
        res = set(nums1) & set(nums2)
        if len(res) == 0:
            return -1
        else :
            return min(res)
# @lc code=end

