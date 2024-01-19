#
# @lc app=leetcode.cn id=2535 lang=python3
#
# [2535] 数组元素和与数字和的绝对差
#

# @lc code=start
class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        res = 0 
        for i in (nums):
            if i >= 10:
                str_i = str(i)
                # res +=  9*(len(str_i)-1)*int(str_i[:-1])
                res += abs(i - sum([int(j) for j in str_i]))
            
        return res 
        
        
        
        
        
# @lc code=end

