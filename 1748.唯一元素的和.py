'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-27 22:18:56
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-16 23:00:55
FilePath: \Leetcode_Solver\1748.唯一元素的和.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1748 lang=python3
#
# [1748] 唯一元素的和
#

# @lc code=start
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        
        import collections
        
        if len(set(nums)) == len(nums):
            return sum(nums)
        elif len(set(nums)) == 1 :
            return 0
        else :
            # res = 0
            # for i in collections.Counter(nums).keys():
            #     if collections.Counter(nums)[i] == 1:
            #         res += i
            # return res
            counts = [0]*101
            total = 0;
            for i in nums:
                if counts[i] == 0:
                    total += i
                elif counts[i] == 1:
                    total -= i
                else :
                    pass 
                counts[i] += 1 
                # print(total)
            return total
       
                    
        
        
        
# @lc code=end

