'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-21 10:33:52
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-21 10:43:34
FilePath: \Leetcode_Solver\2037.使每位学生都有座位的最少移动次数.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=2037 lang=python3
#
# [2037] 使每位学生都有座位的最少移动次数
#

# @lc code=start
class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        
        # 
        # count = 0
        # for student in students:
        #     if student in seats:
        #         seats.remove(student)
        #         students.remove(student)
                
        # for student in students:
        #         dist = [seat - student for seat in seats]
        #         min_dist = min(dist,key=lambda x:(abs(x),x))
        #         seats.remove(min_dist+student)
        #         count+=abs(min_dist)
                
        #         print(dist)
                
        # return count
        
# @lc code=end

