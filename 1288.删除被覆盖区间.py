#
# @lc app=leetcode.cn id=1288 lang=python3
#
# [1288] 删除被覆盖区间
#

# @lc code=start
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        
        # 按照起点升序排列，起点相同时降序排列
        intervals.sort(key=lambda a: (a[0], -a[1]))
        
        
        # 记录合并区间的起点和终点
        left, right = intervals[0][0], intervals[0][1]
        res = 0
        for i in range(1, len(intervals)):
            intv = intervals[i]
            # 情况一，找到覆盖区间
            if left <= intv[0] and right >= intv[1]:
                res += 1
            # 情况二，找到相交区间，合并
            if right >= intv[0] and right <= intv[1]:
                right = intv[1]
            # 情况三，完全不相交，更新起点和终点
            if right < intv[0]:
                left, right = intv[0], intv[1]
                
        return len(intervals) - res
        
        
        
        
# @lc code=end

