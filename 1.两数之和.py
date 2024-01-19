#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2:
            return [0,1]
        
        res_dict = {} 
        for i in range(len(nums)):
            res_dict[nums[i]] = i

        for i in range(len(nums)):
            if target % 2 == 0 and target //2 == nums[i]:
                for j in range(i+1,len(nums)):
                    if nums[i] == nums[j]:
                        return [i,j]
            else:
                rest = target - nums[i]
                if rest in res_dict.keys():
                    return [i,res_dict[rest]]
        
        
        # all_nums = sorted(nums)
        # left,right = 0,len(all_nums)-1
        # while(left <right):
        #     if all_nums[left] + all_nums[right] == target:
        #         return [res_dict[all_nums[left]], res_dict[all_nums[right]]]
        #     elif all_nums[left] + all_nums[right] < target:
        #         left += 1
        #     elif all_nums[left] + all_nums[right] > target:
        #         right -= 1
        
        
        # all = [0]* 1000
        # for i in range(len(nums)):
        #     all[nums[i]] = i
        
        # for i in range(target):
        #     if all[i] and all[target-i]:
        #         return [all[i],all[target-i]]
            
            
            
        
# @lc code=end

