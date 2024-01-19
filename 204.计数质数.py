#
# @lc app=leetcode.cn id=204 lang=python3
#
# [204] 计数质数
#

# @lc code=start
class Solution:
    def countPrimes(self, n: int) -> int:
        res=[]
        adder=0
        for i in range(0,n+1):
            res.append(adder)
            if self.is_prime(i):
                adder+=1
        return res[i]


    def is_prime(self,n):
        if n < 2 :
            return False
        if n == 2:
            return True

        for i in range(2,n):
            if n % i ==0:
                return False
        return True

        #  res=[0,0,0,1,2,2,3,3,4,4,4,4,5]

# @lc code=end

