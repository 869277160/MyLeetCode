#
# @lc app=leetcode.cn id=2639 lang=python3
#
# [2639] 查询网格图中每一列的宽度
#

# @lc code=start
class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        # return [max(len(str(x)) for x in col) for col in zip(*grid)]
        res = []
        for col in range(len(grid[0])):
            # res.append(0)
            temp = []
            for row in range(len(grid)):
                temp.append(len(str(grid[row][col])))
            res.append(max(temp))
        return res 
# @lc code=end

