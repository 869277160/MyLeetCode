#
# @lc app=leetcode.cn id=526 lang=python3
#
# [526] 优美的排列
#

# @lc code=start
class Solution:
    def countArrangement(self, n: int) -> int:
        if n == 1 or n == 2 :
            return n
        nums = [i for i in range(1,n+1)]
        self.res = 0
        for i in range(len(nums)):
            self.helper(nums[:i] + nums[i+1:], nums[i], 2)
        
        return self.res
        
    def helper(self, nums:list, current_num:int, current_pos:int):
        # print(nums,current_num,current_pos,self.res)
        if len(nums) == 1:
            if nums[-1] % current_pos == 0 or current_pos % nums[-1] == 0:
                self.res +=1
            
        # elif len(nums) == 2:
        #     if (nums[0] % current_pos == 0 or current_pos % nums[-1] == 0) or \
        #         (nums[-1] % current_pos+1 == 0 or current_pos+1 % nums[-1] == 0):
        #             self.res +=1
        else:
            if current_num % current_pos == 0 or current_pos % current_num == 0:
    
                current_pos += 1
                for i in range(len(nums)):
                    self.helper(nums[:i] + nums[i+1:], nums[i], current_pos)
            else :
                return 
        
        
        
# @lc code=end

