#
# @lc app=leetcode.cn id=2027 lang=python3
#
# [2027] 转换字符串的最少操作次数
#

# @lc code=start
class Solution:
    def minimumMoves(self, s: str) -> int:
        if "X" not in s :
            return 0
        else:
            count = 0 
            pos = 0
            while pos < len(s):
                if s[pos] == "X":
                    count += 1
                    pos += 3
                else:
                    pos += 1
            return count
# @lc code=end

