#
# @lc app=leetcode.cn id=342 lang=python3
#
# [342] 4的幂
#

# @lc code=start
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        
        if n == 0: return False 
        if n == 1: return True 
        if n % 2 == 1: return False
        if(n<=0): return False
        while(n%64==0):
                n/=64
        while(n%4==0):
            n/=4;
            
        return n==1

        
        
        
# @lc code=end

