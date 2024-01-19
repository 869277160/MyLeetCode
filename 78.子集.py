#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = [[]]
        if len(nums) == 0:
            return self.res
        
        self.res.append(nums)
        if len(nums) == 1:
            return self.res 
        else:
            self.subsetHelper(nums,[],len(nums))
            return self.res 
    
    def subsetHelper(self,nums,temp,length):
        
        # 结束条件（子集特征）
        # 结束条件为所生成序列长度小于候选集合 
        if len(temp) < length and temp != []:
            self.res.append(temp)
        
        # 利用切片操作代替搜索剪枝，遍历所有候选集
        for i in range(len(nums)):
            # 进一步 遍历还没有被遍历过的元素集合组成的子树
            self.subsetHelper(nums[i+1:], temp + [nums[i]],length)
        
# @lc code=end

