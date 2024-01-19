'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-16 22:32:43
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-16 22:35:14
FilePath: \Leetcode_Solver\1046.最后一块石头的重量.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1046 lang=python3
#
# [1046] 最后一块石头的重量
#

# @lc code=start
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while(len(stones)>1):
            if stones[-1] == stones[-2]:
                stones = stones[:-2]
            else:
                stones = stones[:-2] + [stones[-1] - stones[-2]]
            stones.sort()
        
        return stones[0] if stones else 0
# @lc code=end

