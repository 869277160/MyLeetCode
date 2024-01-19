'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-16 13:27:39
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-16 13:33:24
FilePath: \Leetcode_Solver\941.有效的山脉数组.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=941 lang=python3
#
# [941] 有效的山脉数组
#

# @lc code=start
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        if len(arr) < 3:
            return False 
        elif  len(arr) == 3:
            if arr[0] < arr[1] and arr[1] > arr[2]:
                return True
            else:
                return False
        else :
            
            total_len = len(arr)
            left,right = 0, len(arr) - 1;
            # //从左边往右边找，一直找到山峰为止
            while (left + 1 < total_len and arr[left] < arr[left + 1]):
                left += 1
            # //从右边往左边找，一直找到山峰为止
            while (right > 0 and arr[right - 1] > arr[right]):
                right -= 1
            # //判断从左边和从右边找的山峰是不是同一个
            return left >0 and right < total_len -1 and left == right

            
            
            # for i in range(1,len(arr)-2):
            #     if self.isStrictlyIncreasing(arr[:i+1]) and self.isStrictlyDecreasing(arr[i+1:]):
            #         return True
            
            # return False 
    
    def isStrictlyIncreasing(self, input_list):
        
        for i in range(0,len(input_list)-1):
            if input_list[i] >= input_list[i+1]:
                return False
        return True
                
    def isStrictlyDecreasing(self, input_list):
        
        for i in range(0,len(input_list)-1):
            if input_list[i] <= input_list[i+1]:
                return False
        
        return True
# @lc code=end

