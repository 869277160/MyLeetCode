'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-21 23:35:41
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-22 09:25:51
FilePath: \Leetcode_Solver\2150.找出数组中的所有孤独数字.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2150 lang=python3
#
# [2150] 找出数组中的所有孤独数字
#

# @lc code=start
from collections import Counter


class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        
        
        num_dict = {}
        for i in nums :
            if i not in num_dict.keys():
                num_dict[i] = 0
            num_dict[i] +=1
        
        temp_res = [i for i in num_dict.keys() if num_dict[i] == 1]
        res = []
        for i in temp_res:
            if i+1 not in nums and i-1 not in nums:
                res.append(i)
        
        return res 
        
        # res =  []
        
        # for i in range(len(nums)):
        #     if nums[i] not in nums[:i] and nums[i] not in nums[i+1:]:
        #         if nums[i]+1 not in nums and nums[i]-1 not in nums:
        #             res.append(nums[i])
        
        
        # return res
        
        
        
        # book = Counter(nums)
        # return [
        #     num
        #     for num, freq in book.items()
        #     if freq == 1 > book[num - 1] + book[num + 1]
        # ]
        
# @lc code=end

