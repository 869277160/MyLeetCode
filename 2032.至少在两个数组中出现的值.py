'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-20 15:59:01
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-20 16:02:47
FilePath: \Leetcode_Solver\2032.至少在两个数组中出现的值.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2032 lang=python3
#
# [2032] 至少在两个数组中出现的值
#

# @lc code=start
class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        res = []
        
        # # 1. 暴力法
        # for i in range (1,101):
        #     if i in nums1 and i in nums2:
        #         res.append(i)
        #     elif i in nums1 and i in nums3:
        #         res.append(i)
        #     elif i in nums2 and i in nums3:
        #         res.append(i)
                
        # return res 
        
        
        ## 2. 用集合
        set12 = set(nums1) & set(nums2)
        set13 = set(nums1) & set(nums3)
        set23 = set(nums2) & set(nums3)
        
        return list(set12 | set13 | set23)



# @lc code=end

