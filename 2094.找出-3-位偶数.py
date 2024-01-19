#
# @lc app=leetcode.cn id=2094 lang=python3
#
# [2094] 找出 3 位偶数
#

# @lc code=start
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        import collections
        
        digits_counter = collections.Counter(digits)
        
        res = []
        for i in range(100,1000):
            if i % 2 == 0:
                num_counter = collections.Counter([int(j) for j in str(i)])
                if num_counter & digits_counter == num_counter:
                    res.append(i)
        
        return res 
        
        
        
# @lc code=end

