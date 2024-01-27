#
# @lc app=leetcode.cn id=90 lang=python3
#
# [90] 子集 II
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        if nums == []:
            return []
        
        # 有重复的元素时需要先进行排序
        nums.sort()
        
        self.res = []
        self.traverse(nums, 0, [])
        return self.res
    
    def traverse(self, nums: List[int], current_idx: int, track: List[int]):
        # print(candidates, current_idx)
        # print(track, sum(track))
        self.res.append(track[:])
        
        for i in range(current_idx,len(nums)):
            # 如果有重复元组，只使用第一个
            if i > current_idx and nums[i] == nums[i-1]:
                    continue
            track.append(nums[i])
            self.traverse(nums[i+1:], current_idx, track)
            track.pop()
        
# @lc code=end

