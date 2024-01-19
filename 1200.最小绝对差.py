'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-20 22:54:18
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-20 23:00:58
FilePath: \Leetcode_Solver\1200.最小绝对差.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=1200 lang=python3
#
# [1200] 最小绝对差
#

# @lc code=start
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr = sorted(arr)
        
        # diff = [arr[i+1]- arr[i] for i in range(len(arr)-1)]
        
        # res = []
        # for i in range(len(diff)):
        #     if diff[i] == min(diff):
        #         res.append([arr[i],arr[i+1]])
        
        # return res 
        
        ans=[]
        min_num=float('inf')
        for i in range(1,len(arr)):
            temp=arr[i]-arr[i-1]
            if temp<=min_num:
                if temp<min_num:
                    while len(ans):
                        ans.pop()
                min_num=temp
                ans.append([arr[i-1],arr[i]])
        return ans
        
        
        
# @lc code=end

