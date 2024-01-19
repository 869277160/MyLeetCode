#
# @lc app=leetcode.cn id=1791 lang=python3
#
# [1791] 找出星型图的中心节点
#

# @lc code=start
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
      

        dict_count = {}
        
        for i in range(len(edges)):
            if edges[i][0] not in dict_count:
                dict_count[edges[i][0]] = 1
            else:
                dict_count[edges[i][0]] += 1
            if edges[i][1] not in dict_count:
                dict_count[edges[i][1]] = 1
            else:
                dict_count[edges[i][1]] += 1
                
        for k,v in dict_count.items():
            if v == len(edges):
                return k

   

# @lc code=end

