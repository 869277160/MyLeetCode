#
# @lc app=leetcode.cn id=867 lang=python3
#
# [867] 转置矩阵
#

# @lc code=start
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        
        return zip(*matrix)
        # m, n = len(matrix), len(matrix[0]) #转置矩阵的长和宽颠倒
        # res = [[0] * m for _ in range(n)]
        # for i in range(m):
        #     for j in range(n):
        #         res[j][i] = matrix[i][j]
        # return res
# @lc code=end

