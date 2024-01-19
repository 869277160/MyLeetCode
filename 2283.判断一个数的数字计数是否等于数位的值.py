#
# @lc app=leetcode.cn id=2283 lang=python3
#
# [2283] 判断一个数的数字计数是否等于数位的值
#

# @lc code=start
class Solution:
    def digitCount(self, num: str) -> bool:
        
        import collections
        freq = collections.Counter(num)
        return all([int(num[i]) == freq[str(i)] for i in range(len(num))])
        
        
        
# @lc code=end

