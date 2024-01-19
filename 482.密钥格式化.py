#
# @lc app=leetcode.cn id=482 lang=python3
#
# [482] 密钥格式化
#

# @lc code=start
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        
        words = s.split("-")
        
        rest = "".join(words).upper()
        
        head = len(rest) % k
        res = ""
        for i in range(len(rest),head,-k):
            res = "-" + rest[i-k:i] + res
        
        if head == 0:
            return res[1:]
        else :
            return rest[:head] + res
        
        
        
        
# @lc code=end

