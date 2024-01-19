#
# @lc app=leetcode.cn id=1869 lang=python3
#
# [1869] 哪种连续子字符串更长
#

# @lc code=start
class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        
        return max([len(i) for i in s.split('0')]) > max([len(i) for i in s.split('1')])
        
        
        
        
        
# @lc code=end

