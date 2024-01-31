#
# @lc app=leetcode.cn id=2595 lang=python3
#
# [2595] 奇偶位数
#

# @lc code=start
class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        res = [0,0]
        for i in range(len(str(bin(n))[2:])):
            if str(bin(n))[2:][::-1][i] == "1":
                res[i % 2] += 1
        return res 
        
# @lc code=end

