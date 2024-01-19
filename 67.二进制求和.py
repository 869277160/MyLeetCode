#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_int=int(a,base=2);
        b_int=int(b,base=2);
        total=a_int+b_int;
        total=bin(total)
        out=str(total)
        out=out.replace("0b","")

        return out
# @lc code=end

