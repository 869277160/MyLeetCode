#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # if nums:
        #     for i in range(len(nums)):
        #         for j in range(i+1,len(nums)):
        #             if i + j == target:
        #                 return [i,j]
        all = [0]* 1000
        for i in range(len(nums)):
            all[nums[i]] = i
        
        for i in range(target):
            if all[i] and all[target-i]:
                return [all[i],all[target-i]]
            
            
            
        
# @lc code=end

