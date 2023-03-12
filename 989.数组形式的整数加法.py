#
# @lc app=leetcode.cn id=989 lang=python3
#
# [989] 数组形式的整数加法
#

# @lc code=start
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        
        def list2int(nums):
            res = 0
            for i in nums:
                res = res * 10 + i
            return res 
        
        def int2list(total):
            res = []
            while total:
                res.append(total % 10)
                total //= 10

            return res[::-1] if res else [0]
        
        return int2list(list2int(num) + k)
        
        
# @lc code=end

