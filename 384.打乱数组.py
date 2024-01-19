'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-24 17:06:53
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-24 17:12:37
FilePath: \Leetcode_Solver\384.打乱数组.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=384 lang=python3
#
# [384] 打乱数组
#

# @lc code=start
from random import shuffle

class Solution:
    def __init__(self, nums: List[int]):
        
        self.all_nums = [i for i in nums]
        self.init_state = [i for i in nums]
        
    def reset(self) -> List[int]:
        self.all_nums = [i for i in self.init_state]
        return self.init_state

    def shuffle(self) -> List[int]:
        shuffle(self.all_nums)
        return self.all_nums



# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
# @lc code=end

