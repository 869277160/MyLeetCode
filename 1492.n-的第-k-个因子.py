#
# @lc app=leetcode.cn id=1492 lang=python3
#
# [1492] n 的第 k 个因子
#

# @lc code=start
import math 

class Solution:
    def kthFactor(self, n: int, k: int):
        res = [1,n]
        
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                res.append(i)
                res.append(n//i)

        res = sorted(list(set(res)))
        
        if k-1 >= len(res):
            return -1 
        else :
            return res[k-1]
        
# @lc code=end

