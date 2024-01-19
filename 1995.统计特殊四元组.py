'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-16 23:38:17
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-16 23:38:51
FilePath: \Leetcode_Solver\1995.统计特殊四元组.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1995 lang=python3
#
# [1995] 统计特殊四元组
#

# @lc code=start
class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        
        count = 0
        for i in range (len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    for l in range(k+1,len(nums)):
                        if nums[i] + nums[j] + nums[k] == nums[l]:
                            count += 1
        return count


# @lc code=end

