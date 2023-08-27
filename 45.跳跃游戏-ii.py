'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-08-25 16:02:10
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-08-25 16:10:00
FilePath: \Leetcode_Solver\45.跳跃游戏-ii.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#
from typing import List 
# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        length = len(nums)
        if not nums:
            return 0
        else:
            jump = 0
            current = 0
            next = 0
            
            for i in range(length):
                if current < i:
                    jump += 1
                    current = next
                
                next = max(next, i + nums[i])
        
        return jump


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.jump([2,3,1,1,4]))