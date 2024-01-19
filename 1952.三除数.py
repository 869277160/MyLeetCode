#
# @lc app=leetcode.cn id=1952 lang=python3
#
# [1952] 三除数
#

# @lc code=start
class Solution:
    def isThree(self, n: int) -> bool:
        if n <3:
            return False 
        
        if (int(n**0.5))**2 != n:
            return False
        else :
            for i in range(2, int(int(n**0.5)**0.5)+1):
                if int(n**0.5) % i == 0:
                    return False

            return True 
        
        
# @lc code=end

