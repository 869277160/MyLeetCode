'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-01 09:23:59
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-01 09:30:12
FilePath: \Leetcode_Solver\1184.公交站间的距离.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1184 lang=python3
#
# [1184] 公交站间的距离
#

# @lc code=start
class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start > destination:
            start, destination = destination, start
        return min(sum(distance[start:destination]), sum(distance[:start]) + sum(distance[destination:]))


    # def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:

    #     round_distance = distance + distance
        
    #     direct_distance = sum(distance[start:destination])
    #     undirect_distance = sum(round_distance[start:destination+len(distance)])
        
    #     return min(direct_distance, undirect_distance)


    #     # total = sum(distance)
    #     # direct_distance = 
    #     # res = min(total-(direct_distance),(direct_distance))
        
    
    
    #     return res 
        
# @lc code=end

