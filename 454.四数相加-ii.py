'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-14 09:20:22
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-14 09:23:05
FilePath: \Leetcode_Solver\454.四数相加-ii.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=454 lang=python3
#
# [454] 四数相加 II
#

# @lc code=start
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        
        # total = 0
        # for i in (nums1):
        #     for j in (nums2):
        #         for k in (nums3):
        #             for l in (nums4):
        #                 if i+j+k+l == 0:
        #                     total += 1
        # return total
        
        import collections
        countAB = collections.Counter(u + v for u in nums1 for v in nums2)
        ans = 0
        for u in nums3:
            for v in nums4:
                if -u - v in countAB:
                    ans += countAB[-u - v]
        return ans

        
        
        
        
        
# @lc code=end

