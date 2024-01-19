#
# @lc app=leetcode.cn id=396 lang=python3
#
# [396] 旋转函数
#

# @lc code=start

        
        
        
        
class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        # F(k + 1) = F(k) + sum(nums) - n * nums[-k]
        n, s, f = len(nums), sum(nums), sum(i * num for i, num in enumerate(nums))
        ans = f
        for i in range(1, n):
            f += s - n * nums[-i]
            ans = max(ans, f)
        return ans
    
        # f(i) - f(i - 1) = sum(nums) - n * nums[n - i]
    
# @lc code=end

