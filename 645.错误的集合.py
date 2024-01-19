'''
Author: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
Date: 2023-02-07 11:09:07
LastEditors: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
LastEditTime: 2023-02-07 11:39:41
FilePath: \Leetcode_Solver\645.错误的集合.py
Description: 
'''
#
# @lc app=leetcode.cn id=645 lang=python3
#
# [645] 错误的集合
#

# @lc code=start
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        count = [False] * 20000
        dup = 0
        
        
        for i in nums:
            if not count[i]:
                count[i] = True
            else :
                dup = i
        
        for i in range(1, 20000+1):
            if not count[i]:
                return [dup,i]
        
# @lc code=end

