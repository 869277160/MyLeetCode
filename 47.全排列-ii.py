#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
       
        if len(nums) == 0: return []
        elif len(nums) == 1: return [[nums]]
        elif len(nums) == 2: 
            if nums[0] == nums[1]:
                return [nums]
            else :
                return [nums,nums[::-1]]
        else :
            self.res = []
            nums = sorted(nums)
            self.backtrack(nums,[])
            
            return self.res
        
   
    def backtrack(self,nums, tmp):
        if not nums:
            self.res.append(tmp)
            return 
        
        for i in range(len(nums)):
            # 遍历除了自己之外的子树
            next_unique_index = self.get_unique(nums,i)
            if next_unique_index != len(nums):
                self.backtrack(nums[:i] + nums[next_unique_index:], tmp + [nums[i]])
            else :
                self.backtrack(nums[:i], tmp + [nums[i]])
        
    def get_unique(self,nums,i):
        
        for j in range(i,len(nums)):
            if nums[i] != j:
                return j
        
        return len(nums)
    # 自己的废稿子
    # def permuteHelper(self,nums: List[int],track,used):
        
    #     if len(track) == len(nums):
    #         self.res.append(track)
    #         # self.track = []
    #         return 

    #     for i in range(len(nums)):
    #         if used[i]: continue
                
    #         track.append(nums[i])
    #         used[i] = True
                
    #         self.permuteHelper(nums,track)
                
                
    #         track = track[:-2]
    #         used[i] = False 
            
        
        
# @lc code=end

