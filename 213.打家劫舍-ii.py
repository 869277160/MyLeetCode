'''
Author: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
Date: 2023-02-05 15:52:55
LastEditors: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
LastEditTime: 2023-02-05 16:02:04
FilePath: \Leetcode_Solver\213.打家劫舍-ii.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=213 lang=python3
#
# [213] 打家劫舍 II
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        
        rob_all = [0 for i in range(len(nums))]
        # 手动设置尾部和头部相连
        for i in range(len(rob_all)):
            rob_all[i] = rob_all[i] + rob_all[i-2]
            rob_all[i] = max(rob_all[i],rob_all[i-1])
            
        return rob_all[-1]
        
        
        
        
# @lc code=end

