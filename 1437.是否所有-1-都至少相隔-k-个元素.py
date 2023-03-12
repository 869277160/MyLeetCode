'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-27 12:01:11
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-27 12:06:49
FilePath: \Leetcode_Solver\1437.是否所有-1-都至少相隔-k-个元素.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1437 lang=python3
#
# [1437] 是否所有 1 都至少相隔 k 个元素
#

# @lc code=start
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        last = -1 
        
        
        for i in range(0, len(nums)):
            if nums[i] == 0 :
                pass 
            if nums[i] == 1 :
                if last==-1:
                    last = i
                else:
                    if k >= i-last:
                        return False
                    else :
                        last = i
                            
        
        return True 
        
# @lc code=end

