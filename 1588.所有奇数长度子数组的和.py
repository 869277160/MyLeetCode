'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-18 15:47:08
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-21 14:58:07
FilePath: \Leetcode_Solver\1588.所有奇数长度子数组的和.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1588 lang=python3
#
# [1588] 所有奇数长度子数组的和
#

# @lc code=start
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        
        if len(arr) == 1 or len(arr) == 2:
            return sum(arr)
        if len(arr) == 3:
            return 2* sum(arr)
        
        # res = 0
        # total_len = len(arr)
        # groups = total_len //2 
        # for i in range(total_len):
        #     res += arr[i]
        #     for j in range(3,len(arr)+1,2):
                
                
                
        
        
        total = 0
        n = len(arr)
        for i, v in enumerate(arr):
            leftCount, rightCount = i, n - i - 1
            leftOdd = (leftCount + 1) // 2
            rightOdd = (rightCount + 1) // 2
            leftEven = leftCount // 2 + 1
            rightEven = rightCount // 2 + 1
            freq = (leftOdd * rightOdd + leftEven * rightEven)
            print(leftOdd, rightOdd, leftEven, rightEven)
            print(freq)
            total += v * freq
        return total

        # 暴力求解
        # res = sum(arr) if len(arr) % 2 == 0 else sum(arr)*2
        
        # for i in range(3, len(arr)-1, 2):
        #     for j in range(0, len(arr)-i+1):
        #         res += sum(arr[j:j+i])

        # return res 
# @lc code=end

