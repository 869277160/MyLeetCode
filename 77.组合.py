'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-12 22:51:41
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-12 23:18:02
FilePath: \Leetcode_Solver\77.组合.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k == 1:
            return [[i] for i in range(1,n+1)]
        elif k == n:
            return [[i for i in range(1,n+1)]]
        else :
            self.res = []
            nums = [i for i in range(1,n+1)]
            self.combineHelper(nums,k,[])
            
            return self.res 
        
    def combineHelper(self,nums,k,temp):
        
        # 结束条件为所生成序列长度和候选集合相同
        if len(temp) == k:
            self.res.append(temp)
        
        # 遍历所有候选集
        for i in range(len(nums)):
            # 进一步 遍历还没有被遍历过的集合组成的子树
            self.combineHelper(nums[i+1:], k, temp + [nums[i]])
        
        
# @lc code=end

