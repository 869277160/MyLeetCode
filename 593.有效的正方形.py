#
# @lc app=leetcode.cn id=593 lang=python3
#
# [593] 有效的正方形
#

# @lc code=start
class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        
        dist_2 = abs(p1[0] - p2[0]) ** 2 + abs(p1[1] - p2[1]) ** 2
        dist_3 = abs(p1[0] - p3[0]) ** 2 + abs(p1[1] - p3[1]) ** 2
        dist_4 = abs(p1[0] - p4[0]) ** 2 + abs(p1[1] - p4[1]) ** 2
        

        v14 = [p4[0] - p1[0], p4[1] - p1[1]]
        
        if (dist_2 == dist_3 and dist_2 != dist_4):
            v12 = [p2[0] - p1[0], p2[1] - p1[1]]
            v13 = [p3[0] - p1[0], p3[1] - p1[1]]
            
            v42 = [p2[0] - p4[0], p2[1] - p4[1]]
            v43 = [p3[0] - p4[0], p3[1] - p4[1]]
            
            if v12[1] * v13[1] == -v12[0] * v13[0] and v42[1] * v43[1] == -v42[0] * v43[0]:
               return True
            else:
                return False 

        if (dist_2 == dist_4 and  dist_2 != dist_3):
            
            v12 = [p2[0] - p1[0], p2[1] - p1[1]]
            v14 = [p4[0] - p1[0], p4[1] - p1[1]]
            
            v32 = [p2[0] - p3[0], p2[1] - p3[1]]
            v34 = [p4[0] - p3[0], p4[1] - p3[1]]
            
            if v12[1] * v14[1] == -v12[0] * v14[0] and v32[1] * v34[1] == -v32[0] * v34[0]:
               return True
            else:
                return False 

        
        if (dist_3 == dist_4 and  dist_2 != dist_3):
            v14 = [p4[0] - p1[0], p4[1] - p1[1]]
            v13 = [p3[0] - p1[0], p3[1] - p1[1]]
            
            v24 = [p4[0] - p2[0], p4[1] - p2[1]]
            v23 = [p3[0] - p2[0], p3[1] - p2[1]]
            
            if v14[1] * v13[1] == -v14[0] * v13[0] and v23[1] * v24[1] == -v23[0] * v24[0]:
               return True
            else:
                return False 
            
        return False 
# @lc code=end

