#
# @lc app=leetcode.cn id=2644 lang=python3
#
# [2644] 找出可整除性得分最大的整数
#

# @lc code=start
class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        max_cnt, ans = -1, 0
        for d in divisors:
            cnt = sum(x % d == 0 for x in nums)
            if cnt > max_cnt or cnt == max_cnt and d < ans:
                max_cnt, ans = cnt, d
        return ans

# @lc code=end

