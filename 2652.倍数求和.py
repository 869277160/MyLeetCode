#
# @lc app=leetcode.cn id=2652 lang=python3
#
# [2652] 倍数求和
#

# @lc code=start
class Solution:
    def sumOfMultiples(self, n: int) -> int:
        if n < 3 :
            return 0
        res = 0
        for i in range(3, n+1):
            # print(res)
            if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
                res += i
                # print(i)
        return res 
        
# @lc code=end

