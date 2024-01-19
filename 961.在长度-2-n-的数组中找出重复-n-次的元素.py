'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-20 09:51:22
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-20 20:16:12
FilePath: \Leetcode_Solver\961.在长度-2-n-的数组中找出重复-n-次的元素.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=961 lang=python3
#
# [961] 在长度 2N 的数组中找出重复 N 次的元素
#

# @lc code=start
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        
        import collections
        
        freq = collections.Counter(nums)
        
        return freq.most_common(1)[0][0]
        
        # nums = sorted(nums)
        # more = nums[0]
        # count = 1
        
        # for i in nums:
        #     if more == i:
        #         count +=1
        #     else :
        #         more = i
        #         count -= 1
                
        #     if count == len(nums) //2:
        #         return more
        
        # return more

    
        nums = sorted(nums)
        if nums[len(nums)//2] == nums[len(nums)//2 -1]:
            return nums[len(nums)//2 ]
        else :
            return nums[len(nums)//2-1]

# @lc code=end

