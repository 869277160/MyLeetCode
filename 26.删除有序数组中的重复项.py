'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-13 09:18:16
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-13 09:37:37
FilePath: \Leetcode_Solver\26.删除有序数组中的重复项.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除有序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        # 快慢指针遍历，
        # 快指针遍历，慢指针记录不重复的元素所需要放置的位置。
        slow = 0
        for fast in range((len(nums))):
            if nums[fast] == nums[slow]:
                continue;
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
        
        return slow+1
        
# @lc code=end

