#
# @lc app=leetcode.cn id=2970 lang=python3
#
# [2970] 统计移除递增子数组的数目 I
#

# @lc code=start
class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        
        if self.is_inc(nums):
            return len(nums) * (len(nums)+1) // 2
        
        n=len(nums)
        ans=0
        for i in range(n):
            for j in range(i,n):
                temp=nums[:i]+nums[j+1:]
                if self.is_inc(temp):
                    ans+=1
        return ans


    def is_inc(self, nums):
        if nums != []:
            for i in range(1,len(nums)):
                if nums[i] <= nums[i-1]:
                    return False 
                
        return True 
        
        
# @lc code=end

