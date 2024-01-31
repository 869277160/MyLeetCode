#
# @lc app=leetcode.cn id=2916 lang=python3
#
# [2916] 子数组不同元素数目的平方和 II
#

# @lc code=start
class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            res += 1
            collects = 1 
            for j in range(i+1,len(nums)):
                # print(nums[j], nums[i:j])
                if nums[j] not in nums[i:j]:
                    collects += 1
                res += (collects ** 2) % ( 1_000_000_007)
                    
        
        return int(res) 
# @lc code=end

