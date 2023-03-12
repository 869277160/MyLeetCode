#
# @lc app=leetcode.cn id=168 lang=python3
#
# [168] Excel表列名称
#



# @lc code=start
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        # 转26进制
        all_chr = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        if columnNumber < 27:
            return all_chr[columnNumber]
        else :
            res = ""
            while columnNumber > 0:
                a0 = (columnNumber - 1) % 26 + 1
                res = all_chr[a0] + res 
                columnNumber = (columnNumber - a0) // 26
            return res
            
         
# @lc code=end

