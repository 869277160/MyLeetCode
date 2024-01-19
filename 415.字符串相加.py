'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-16 21:43:04
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-16 22:01:22
FilePath: \Leetcode_Solver\415.字符串相加.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=415 lang=python3
#
# [415] 字符串相加
#

# @lc code=start
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 =="0":
            return num2 if num2 != "0" else num1
        
        i, j = 0,0
        nums1 = num1[::-1]
        nums2 = num2[::-1]
        
        res = ""
        adder = 0
        while(i < len(nums1) or j < len(nums2)):
            if i == len(nums1):
                for q in range(j,len(nums2)):
                    current = int(nums2[q]) + adder
                    adder = current // 10 
                    current = current%10
                    res = f"{current}" + res 
                    
                j = len(nums2)
                # return  res
            if j == len(nums2):
                for r in range(i,len(nums1)):
                    current = int(nums1[r]) + adder
                    adder = current // 10 
                    current = current%10
                    res = f"{current}" + res 
                i = len(nums1)
            if i < len(nums1) and j < len(nums2):
                current = int(nums1[i]) +int(nums2[j]) + adder
                adder = current // 10 
                current = current%10
                res = f"{current}" + res 
                i += 1
                j += 1
                # return res

        if adder == 1:
            res = "1" + res 
        
        return res
# @lc code=end

