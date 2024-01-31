#
# @lc app=leetcode.cn id=2760 lang=python3
#
# [2760] 最长奇偶子数组
#

# @lc code=start
class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        # l,r = 0,0
        max_len = 0
        for i in range(len(nums)):
            if nums[i] % 2 ==0:
                for j in range(0,len(nums)-i):
                    # print(i,j, max_len)
                    if nums[i+j] % 2 == j % 2 and threshold >= nums[i+j]:
                        if j + 1 > max_len:
                            max_len = j + 1 
                        else:
                            pass 
                    else:
                        break
        
        return max_len
            
        
        
        
# @lc code=end

