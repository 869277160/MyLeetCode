#
# @lc app=leetcode.cn id=1253 lang=python3
#
# [1253] 重构 2 行二进制矩阵
#

# @lc code=start
class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        n = len(colsum)
        sum_val = 0
        two_num = 0
        for i in range(n):
            if colsum[i] == 2:
                two_num += 1
            sum_val += colsum[i]
        if sum_val != upper + lower or min(upper, lower) < two_num:
            return []
        upper -= two_num
        lower -= two_num
        res = [[0] * n for _ in range(2)]
        for i in range(n):
            if colsum[i] == 2:
                res[0][i] = res[1][i] = 1
            elif colsum[i] == 1:
                if upper > 0:
                    res[0][i] = 1
                    upper -= 1
                else:
                    res[1][i] = 1
        return res

        
    #     res = [[0 for i in range(len(colsum))], 
    #            [0 for i in range(len(colsum))]]
    #     res = self.traverse(res, 0, colsum, upper, lower)

    #     return res if res != [] else res
        
    
    # def traverse(self, res, current_col, colsum, upper, lower):
    #     # print(current_col, res)
    #     if current_col == len(colsum):
    #         if upper == 0 and lower == 0:
    #         # if sum(res[0]) == upper and sum(res[1]) == lower:
    #             return res 
    #         else:
    #             return []
    #     else:
    #         if colsum[current_col] == 0:
    #             res[0][current_col] = 0
    #             res[1][current_col] = 0
    #             return self.traverse(res, current_col+1, colsum, upper, lower)
    #         if colsum[current_col] == 1:
    #             res[0][current_col] = 1
    #             res[1][current_col] = 0
    #             res_1 = self.traverse(res, current_col+1, colsum, upper-1, lower)
                
    #             if res_1 != []:
    #                 return res_1
                
    #             res[0][current_col] = 0
    #             res[1][current_col] = 1
    #             res_2 = self.traverse(res, current_col+1, colsum, upper, lower-1)

    #             return res_2
    #         if colsum[current_col] == 2:
    #             res[0][current_col] = 1
    #             res[1][current_col] = 1
    #             return self.traverse(res, current_col+1, colsum, upper-1, lower-1)
                
        
# @lc code=end

