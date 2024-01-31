#
# @lc app=leetcode.cn id=2980 lang=python3
#
# [2980] 检查按位或是否存在尾随零
#

# @lc code=start
class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        res = [(str(bin(num))[-1]) for num in nums]
        from collections import Counter
        
        return True if Counter(res)["0"] > 1 else False
                
# @lc code=end

