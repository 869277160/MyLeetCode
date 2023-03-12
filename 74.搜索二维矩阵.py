#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m, n = len(matrix), len(matrix[0])
        
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        
        else:
            
            if target >= matrix[0][0] and target <= matrix[0][-1]:
                if target in matrix[0]:
                    return True 
                else :
                    return False 
                
            
            for i in range(1,m):
                
                if target > matrix[i-1][-1] and target < matrix[i][0]:
                    return False
                elif target > matrix[i][-1]:
                    pass
                elif target >= matrix[i][0] and target <= matrix[i][-1]:
                    if target in matrix[i]:
                        return True 
                    else :
                        return False 
                    # 进一步线性搜索
                    # for j in range(1,n):
                    #     if matrix[i][j] == target:
                    #         return True
                    #     if matrix[i][j] > target:
                    #         return False
                    #  再次替换为二分查找
                
                
            return False 

        
        
        
        
        
        
# @lc code=end

