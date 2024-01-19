#
# @lc app=leetcode.cn id=868 lang=python3
#
# [868] 二进制间距
#

# @lc code=start
class Solution:
    def binaryGap(self, n: int) -> int:
        count = bin(n).count("1")
        
        if count < 2 :
            return 0
        else :
            res = 1
            for i in range(len(bin(n))):
                if bin(n)[i] == "1":
                    
                    for j in range(i+1,len(bin(n))):
                        if bin(n)[j] == "1":
                            res = max(res,j-i)
                            break
            return res 
        
        
# @lc code=end

