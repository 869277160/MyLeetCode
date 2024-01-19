'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-20 21:51:01
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-20 21:55:41
FilePath: \Leetcode_Solver\2570.合并两个二维数组-求和法.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2570 lang=python3
#
# [2570] 合并两个二维数组 - 求和法
#

# @lc code=start
class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        import collections
        
        # nums1_dict = collections.defaultdict()
        # nums2_dict = collections.defaultdict()
        
        
        
        
        id1 = [num[0] for num in nums1]
        
        for num in nums2:
            if num[0] in id1:
                nums1[id1.index(num[0])][1] += num[1]
            else:
                nums1.append(num)
        
        nums1 = sorted(nums1,key=lambda x: x[0])
        
        return nums1 
        
# @lc code=end

