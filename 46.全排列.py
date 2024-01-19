'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-12 22:07:04
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-09 09:56:36
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
            self.permuteSolver(nums,[])
            
            return self.res 
    
    # 类似后序遍历的操作 先定义在根节点的操作，之后遍历各个孩子节点
    def permuteSolver(self,nums,track):
        if len(nums) == 0:
            self.res.append(track)
        
        # 设置如何遍历
        for i in range(len(nums)):
            self.permuteSolver(nums[:i] + nums[i+1:], track + [nums[i]],)

    
    # def permute(self, nums: List[int]) -> List[List[int]]:
        
    #     if len(nums) == 0: return []
    #     elif len(nums) == 1: return [[nums[0]]]
    #     elif len(nums) == 2: return [nums,nums[::-1]]
    #     else :
    #         self.res = []
    #         self.backtrack(nums,[])
            
    #         return self.res
            
    # def backtrack(self,nums, tmp):
        
    #     # 结束条件为候选集为空
    #     if not nums:
    #         self.res.append(tmp)
    #         return 
        
    #     # 遍历所有候选集
    #     for i in range(len(nums)):
    #         # 进一步 遍历除了自己之外的子树
    #         self.backtrack(nums[:i] + nums[i+1:], tmp + [nums[i]])
        
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

