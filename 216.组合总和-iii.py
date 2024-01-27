#
# @lc app=leetcode.cn id=216 lang=python3
#
# [216] 组合总和 III
#

# @lc code=start
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]: 
        
        nums = [i for i in range(1,10)]
        if n < sum(nums[:k]) or n > sum(nums[-k:]):
            return []
        self.res = []
        
        for i in range(len(nums)):
            self.traverse(nums[i+1:], [nums[i]], k, n)
        
        return self.res
        
    def traverse(self, nums: List[int], track:List[int], k: int, n:int):
        # print(nums, track)
        if len(track) == k:
            if sum(track) == n:
                self.res.append(list(track))
            return 
        
        for i in range(len(nums)):
            if sum(track) < n:
                self.traverse(nums[i+1:], track + [nums[i]], k, n)
        
# @lc code=end

