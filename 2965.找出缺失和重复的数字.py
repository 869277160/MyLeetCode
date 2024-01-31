#
# @lc app=leetcode.cn id=2965 lang=python3
#
# [2965] 找出缺失和重复的数字
#

# @lc code=start
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        from collections import Counter
        
        n = len(grid)
        grid_list = []
        for row in grid:
            grid_list += row
        
        res_count = Counter(grid_list)
        
        res_1 = res_count.most_common(1)[0][0]
        # print((n**2)*((n)**2+1)//2)
        # print(sum(grid_list))
        res_2 = (n**2)*((n)**2+1)//2 - sum(grid_list) + res_1
        
        return [res_1, res_2]
        
        

# @lc code=end

