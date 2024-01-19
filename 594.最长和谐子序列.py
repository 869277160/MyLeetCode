'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-20 21:03:20
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-20 21:07:37
FilePath: \Leetcode_Solver\594.最长和谐子序列.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=594 lang=python3
#
# [594] 最长和谐子序列
#

# @lc code=start
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        
        nums = sorted(nums)
        import collections
        
        freq = collections.Counter(nums)
        
        all_num_lenth = {}
        for key in freq.keys():
            temp_len1 = 0
            # temp_len2 = 0
            if key+1 in freq.keys():
                temp_len1 = freq[key] + freq[key+1]
            # if key-1 in freq.keys():
            #     temp_len2 = freq[key] + freq[key-1]
            # all_num_lenth[key] = max(temp_len1,temp_len2)

            all_num_lenth[key] = temp_len1
        return max(all_num_lenth.values())
        
        
        
# @lc code=end

