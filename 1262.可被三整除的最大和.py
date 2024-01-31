#
# @lc app=leetcode.cn id=1262 lang=python3
#
# [1262] 可被三整除的最大和
#

# @lc code=start
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        # nums.sort()
        a = [x for x in nums if x % 3 == 0]
        b = sorted([x for x in nums if x % 3 == 1], reverse=True)
        c = sorted([x for x in nums if x % 3 == 2], reverse=True)

        ans = 0
        lb, lc = len(b), len(c)
        for cntb in [lb - 2, lb - 1, lb]:
            if cntb >= 0:
                for cntc in [lc - 2, lc - 1, lc]:
                    if cntc >= 0 and (cntb - cntc) % 3 == 0:
                        ans = max(ans, sum(b[:cntb]) + sum(c[:cntc]))
        return ans + sum(a)

        
# @lc code=end

