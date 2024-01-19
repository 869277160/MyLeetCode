#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if nums == []:
            return [-1, -1]
        if target not in nums:
            return [-1, -1]
        # else:
            # return [nums.index(target), len(nums) - nums[::-1].index(target) - 1]
        else:
            return [self.find_left_bound(nums,target),self.find_right_bound(nums,target)]
    
    
    # def find_elem(self,num,target):
        
        
    def find_left_bound(self,nums,target):
        left, right = 0,len(nums)-1
        
        while(left <= right):
            mid = left + (right - left) //2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid -1 
            elif nums[mid] == target:
                right = mid -1
                
        if left >= len(nums) or nums[left] != target:
            return -1
        return left 
        
    def find_right_bound(self,nums,target):
        
        left, right = 0, len(nums)-1
        
        while(left <= right):
            mid = left + (right - left) //2 
            
            if nums[mid] < target:
                left = mid +1 
            elif nums[mid] > target:
                right = mid -1
            elif nums[mid] == target:
                left = mid +1
            
        if right< 0 or nums[right]!= target:
            return -1
        return right 
        
        
# @lc code=end

