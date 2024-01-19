#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
                
        # 快慢指针遍历，
        # 快指针遍历，慢指针记录非查找值所需要放置的位置。
        slow = 0
        fast = 0
        for fast in range(len(nums)):
            if nums[fast] == 0:
                continue
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1
        
        for i in range(slow,len(nums)):
            nums[i] = 0
        
        
    #     if len(nums) == 1 or len(nums)==0 : return nums
        
    #     # 以块为单位进行调换 
    #     z_left, z_right = 0,0
    #     nz_left, nz_right =0,0
        
    #     # 每次进入需要重新赋值，重新探索边界值。
    #     while(z_right<len(nums)):
    #         z_left, z_right = 0,0
    #         nz_left, nz_right =0,0
    #         z_left, z_right = self.getzeropos(nums,z_right)
    #         nz_left, nz_right = self.getnonozeropos(nums,z_right)
            
    #         temp = nums[z_left:z_right]
    #         nums[z_left:z_right] = nums[nz_left:nz_right]
    #         nums[nz_left:nz_right] = temp
        
        
    # def getFirstZeroPos(nums):
    #     get_left, get_right = False, False
    #     z_left, z_right = 0,0
    #     for i in range(0,len(nums)):
    #         if nums[i] == 0 and get_left == False:
    #             z_left = i 
    #             get_left = True
                
    #         if nums[i] == 0 and nums[i+1] != 0:
    #             z_right = i+1
    #             return z_left, z_right
        
    #     return z_left,len(nums)-1
    
    # def getSecondNonZeroPos(nums):
    #     get_left, get_right = False, False
    #     nz_left, nz_right = 0,0
    #     for i in range(1,len(nums)):
    #         if nums[i] != 0 and nums[i-1] == 0:
    #             z_left = i 
    #             get_left = True
                
    #         if nums[i] == 0 and nums[i+1] != 0:
    #             z_right = i+1
    #             return z_left, z_right
        
# @lc code=end

