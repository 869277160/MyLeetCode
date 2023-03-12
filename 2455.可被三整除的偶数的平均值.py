'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-17 09:58:34
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-17 10:18:38
FilePath: \Leetcode_Solver\2455.可被三整除的偶数的平均值.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2455 lang=python3
#
# [2455] 可被三整除的偶数的平均值
#

# @lc code=start
class Solution:
    def averageValue(self, nums: List[int]) -> int:
        
        # res = []
        # for i in range(0,200):
        #     if 6*i >= max(nums):
        #         if res == []:
        #             return 0
        #         elif 6*i == max(nums):
        #             res.append(6*i)
        #             return int(sum(res)/len(res))
        #         else :
        #             return int(sum(res)/len(res))
        #     if 6*i in nums:
        #         res.append(6*i)
        
        # asum = [n  for n in nums if n % 6 == 0]
        # alen = len(asum)
        # return sum(asum) // alen if alen != 0 else 0
        
# @lc code=end

