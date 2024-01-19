#
# @lc app=leetcode.cn id=2341 lang=python3
#
# [2341] 数组能形成多少数对
#

# @lc code=start
class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        import collections
        freq = collections.Counter(nums)
        
        res = [0,0]
        for key in freq.keys():
            res[0] += freq[key] // 2 
            res[1] += freq[key] % 2
        
        return res 
        
        
# @lc code=end

