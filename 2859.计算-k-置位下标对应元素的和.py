#
# @lc app=leetcode.cn id=2859 lang=python3
#
# [2859] 计算 K 置位下标对应元素的和
#

# @lc code=start
class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
    
        res = 0
        for i in range(len(nums)):
            temp = sum([int(c) for c in str(bin(i))[2:]])
            if temp == k:
                res += nums[i]
        return res
        
# @lc code=end

