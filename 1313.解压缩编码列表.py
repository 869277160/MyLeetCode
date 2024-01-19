#
# @lc app=leetcode.cn id=1313 lang=python3
#
# [1313] 解压缩编码列表
#

# @lc code=start
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        
        res = []
        
        for i in range(0,len(nums),2):
            freq = nums[i]
            num = nums[i+1]
            
            for j in range(freq):
                res += [num]
        
        
        return res 
        
# @lc code=end

