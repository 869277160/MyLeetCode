'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-20 21:56:42
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-20 22:00:57
FilePath: \Leetcode_Solver\2578.最小和分割.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2578 lang=python3
#
# [2578] 最小和分割
#

# @lc code=start
class Solution:
    def splitNum(self, num: int) -> int:
        all_nums = [i for i in str(num)]
        
        all_nums.sort()
        
        nums1 = "".join([all_nums[i] for i in range(0,len(all_nums),2)])
        nums2 = "".join([all_nums[j] for j in range(1,len(all_nums),2)])
    
        return int(nums1) + int(nums2)
        
        
        
        
        
        
# @lc code=end

