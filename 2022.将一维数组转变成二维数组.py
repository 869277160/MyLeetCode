#
# @lc app=leetcode.cn id=2022 lang=python3
#
# [2022] 将一维数组转变成二维数组
#

# @lc code=start
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        
        if len(original) != m*n:
            return []
        else :
            res = []
            for i in range(m):
                res += [original[i*n:(i+1)*n]]
        
            return res
        
# @lc code=end

