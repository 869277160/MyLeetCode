#
# @lc app=leetcode.cn id=1828 lang=python3
#
# [1828] 统计一个圆中点的数目
#

# @lc code=start
class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        
        res = []
        for q in queries:
            count = 0
            for p in points:
                if (p[0]-q[0])**2 + (p[1]-q[1])**2 <= q[2]**2:
                    count += 1
            res.append(count)
            
        return res 
            
        
# @lc code=end

