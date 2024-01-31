#
# @lc app=leetcode.cn id=2303 lang=python3
#
# [2303] 计算应缴税款总额
#

# @lc code=start
class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        
        res = 0
        # current_income = 0
        last_paid = 0
        for bracket in brackets:
            tax_income = min(income,bracket[0]) - last_paid
            if tax_income > 0:
                res += tax_income * 0.01 * bracket[1]
                last_paid = bracket[0]
            else:
                return res 

        return res 
        
# @lc code=end

