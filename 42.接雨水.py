'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-12 15:26:54
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-12 15:50:25
FilePath: \Leetcode_Solver\42.接雨水.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        if len(set(height)) == 1:
            return res 
    
        # # # 暴力法
        res = 0
        # for i in range(1,len(height)-1):
        #     left, right = max(height[:i]), max(height[i+1:])
        #     res += max(min(left,right) - height[i],0)

        # # # 动态规划
        # res = 0
        # l_max, r_max = [0]*(len(height)), [0]*(len(height))
        # l_max[0] = height[0]
        # r_max[-1] = height[-1]
        # for j in range(1,len(height)):
        #     l_max[j] = max(l_max[j-1],height[j])
        # for i in range(len(height)-2,-1,-1):
        #     r_max[i] = max(r_max[i+1],height[i])
        
        # for i in range(1,len(height)-1):
        #     left, right = l_max[i], r_max[i]
        #     res += max(min(left,right) - height[i],0)

        # # # 双指针
        res = 0
        left, right = 0, len(height)-1
        l_max, r_max = height[left], height[right]
        while(left <= right):
            l_max, r_max = max(l_max,height[left]), max(r_max,height[right])
            
            if l_max < r_max:
                res += l_max - height[left]
                left += 1
            else:
                res += r_max - height[right]
                right -= 1
        
        return res 
    
# @lc code=end

