'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-12 22:07:04
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-12 23:37:27
FilePath: \Leetcode_Solver\46.全排列.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        if len(nums) == 0: return []
        elif len(nums) == 1: return [[nums[0]]]
        elif len(nums) == 2: return [nums,nums[::-1]]
        else :
            self.res = []
            self.backtrack(nums,[])
            
            return self.res
            
    def backtrack(self,nums, tmp):
        
        # 结束条件为候选集为空
        if not nums:
            self.res.append(tmp)
            return 
        
        # 遍历所有候选集
        for i in range(len(nums)):
            # 进一步 遍历除了自己之外的子树
            self.backtrack(nums[:i] + nums[i+1:], tmp + [nums[i]])
        
    # def permuteHelper(self,nums: List[int],track,used):
        
    #     if len(track) == len(nums):
    #         self.res.append(track)
    #         # self.track = []
    #         return 

    #     for i in range(len(nums)):
    #         if used[i]: continue
                
    #         track.append(nums[i])
    #         used[i] = True
                
    #         self.permuteHelper(nums,track)
                
                
    #         track = track[:-2]
    #         used[i] = False 
# @lc code=end

