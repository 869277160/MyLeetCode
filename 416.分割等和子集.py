#
# @lc app=leetcode.cn id=416 lang=python3
#
# [416] 分割等和子集
#

# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # 求解如何将数组中划出来一个子集，子集的和为特定值
        
        total = sum(nums)
        if total % 2 != 0:
            return False 
        total = total //2
        
        dp = [[False] * (total + 1) for _ in range(len(nums)+ 1)]

        # base case
        for i in range(len(nums) + 1):
            dp[i][0] = True
        
        
        
        for i in range(1, len(nums)  + 1):
            for j in range(1, total + 1):
                if j - nums[i - 1] < 0:
                    # 背包容量不足，不能装入第 i 个物品
                    dp[i][j] = dp[i - 1][j]
                else:
                    # 装入或不装入背包
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
        return dp[len(nums)][total]
        
        
        
        
# @lc code=end

