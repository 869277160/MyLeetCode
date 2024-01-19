'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-22 14:17:25
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-22 14:32:06
FilePath: \Leetcode_Solver\1103.分糖果-ii.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1103 lang=python3
#
# [1103] 分糖果 II
#

# @lc code=start
class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        
        import math 
        
        # 10000*10000 = 10000000
        res = [0 for i in range(num_people)]
        # max_people = 0 
        rest = 0
        
        current_sum = 0
        for i in range(1,candies):
            current_sum += i
            if current_sum < candies:
                res[(i-1)%num_people] += i
            else:
                rest = candies - current_sum + i
                res[(i-1)%num_people] += rest
                return res 
        
        return res 
                
        # for i in range(0,int(math.sqrt(10000000000))+1):
        #     if i*(i+1)/2 <= candies and candies < (i+1)*(i+2)/2:
        #         res += 
        #         rest = candies - i*(i+1)/2
        #         break
        
        # for i in range(0,int(math.sqrt(10000000000))+1):
        #     if i*(i+1)/2 <= candies and candies < (i+1)*(i+2)/2:
        #         max_people = i 
        #         rest = candies - i*(i+1)/2
        #         break
        

        # for i in range(1,max_people+1):
        #     res[(i-1)%num_people] += i
        
        # last = max_people%num_people
        # res[last] += rest
        
        # return res 
        
        
        
        
        
# @lc code=end

