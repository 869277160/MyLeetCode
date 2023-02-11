#
# @lc app=leetcode.cn id=171 lang=python3
#
# [171] Excel 表列序号
#

# @lc code=start
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        # 本质上是进制转化
        # 26进制转10进制
        # NOTE: 这种简单的题尽量把所有的变量都写在纸上推算一下，保证思路清晰，一次做对。
        res = 0
        total_len = len(columnTitle)
        for i in range(len(columnTitle)):
            res +=  (ord(columnTitle[i]) - ord('A') + 1) * (26 ** (total_len - i -1))
        
        return res
    
    # def ToInt(self,input):
    #     for i in range(26):
        
    
# @lc code=end

