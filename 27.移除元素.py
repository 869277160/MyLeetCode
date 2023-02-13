'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-13 09:22:09
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-13 09:34:52
FilePath: \Leetcode_Solver\27.移除元素.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        # 快慢指针遍历，
        # 快指针遍历，慢指针记录非查找值所需要放置的位置。
        slow = 0
        fast = 0
        for fast in range(len(nums)):
            if nums[fast] == val:
                continue
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
                
        # while(fast < len(nums)):
        #     if nums[fast] != val:
        #         fast += 1
        #     if nums[fast] == val:
        #         fast = self.next_unique(nums,fast+1,val)
        #         if fast == len(nums):
        #             return slow +1
        #         else :
        #             nums[slow] = nums[fast]
        #             slow += 1
        
        return slow
    
    # def next_unique(self,nums,start,val):
    #     for i in range(start,len(nums)):
    #             if nums[i] != val:
    #                 return i 
     
    #     return len(nums)
        
# @lc code=end

