'''
Author: DingWang wangding19@mails.ucas.ac.cn
Date: 2024-01-29 22:18:56
LastEditors: DingWang wangding19@mails.ucas.ac.cn
LastEditTime: 2024-01-29 22:26:21
FilePath: \Leetcode_Solver\2389.和有限的最长子序列.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2389 lang=python3
#
# [2389] 和有限的最长子序列
#

# @lc code=start
class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        
        # nums.sort()
        # min_sum, max_sum = min(nums), sum(nums)
        # res = []
        # for q in queries:
        #     if q < min_sum or q > max_sum:
        #         res.append(0)
        #     elif q > min_sum and q < max_sum:
        #         if q == min_sum:
        #             res.append(1)
        #         elif q == max_sum:
        #             res.append(len(nums))
        #         else:
        #             if q in nums:
        #                 res.append(1)
        #             else :
        #                 res.append(2)
            
        # return res
        
        nums.sort()
        ans = []
        n = len(nums)
        m = len(queries)
        for i in range(m):
            res = 0
            cnt = 0
            for j in range(n):
                res += nums[j]
                if res > queries[i]:
                    break
                cnt += 1
            ans.append(cnt)
        return ans
            
# @lc code=end

