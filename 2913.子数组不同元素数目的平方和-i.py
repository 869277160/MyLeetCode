#
# @lc app=leetcode.cn id=2913 lang=python3
#
# [2913] 子数组不同元素数目的平方和 I
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
                res += (collects ** 2) % (1e9 + 7)
                    
        
        return int(res) 
        
        
# @lc code=end

