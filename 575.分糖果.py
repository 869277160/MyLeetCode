'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-15 18:23:13
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-15 21:18:44
FilePath: \Leetcode_Solver\575.分糖果.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=575 lang=python3
#
# [575] 分糖果
#

# # @lc code=start
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:

        MaxEatType = 0
        CandyTypeCounter = [0] * 200001
        MinCandyType = min(candyType)
        couldEat = len(candyType) // 2

        for i in candyType :
            CandyTypeCounter[(i-100000)] += 1
        

        for i in CandyTypeCounter:
            if i > 0:
                MaxEatType += 1
            
            if MaxEatType >= couldEat:
                return couldEat

        return MaxEatType
    
# class Solution:
#     def distributeCandies(self, candyType: List[int]) -> int:
#         return min(len(set(candyType)), len(candyType) // 2)

        
# @lc code=end

