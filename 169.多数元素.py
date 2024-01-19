#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = [0] * (len(nums)+1)
        
        for i in nums:
            count[i] +=1
            
        return count.index(max(count))
        
    
    # def majorityElement(self, nums: List[int]) -> int:
    #     nums.sort()
    #     return nums[len(nums)//2]
    
    # def majorityElement(self, nums: List[int]) -> int:
    #     count = 0
    #     res =0
        
    #     for i in range(len(nums)):
    #         if count == 0:
    #             res = nums[i]
    #             count +=1
    #         elif res == nums[i]:
    #             count +=1
    #         else:
    #             count -=1
        
    #     return res 
        
# @lc code=end

