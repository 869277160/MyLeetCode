#
# @lc app=leetcode.cn id=1588 lang=python3
#
# [1588] 所有奇数长度子数组的和
#

# @lc code=start
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        
        if len(arr) == 1 or len(arr) == 2:
            return sum(arr)
        if len(arr) == 3:
            return 2* sum(arr)
        
        
        res = sum(arr) if len(arr) % 2 == 0 else sum(arr)*2
        
        for i in range(3, len(arr)-1, 2):
            for j in range(0, len(arr)-i+1):
                res += sum(arr[j:j+i])

        return res 
# @lc code=end

