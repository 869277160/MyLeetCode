#
# @lc app=leetcode.cn id=2815 lang=python3
#
# [2815] 数组中的最大数对和
#

# @lc code=start
class Solution:
    def maxSum(self, nums: List[int]) -> int:
        
        res = [[0,0] for i in range(10)]
        for num in nums:
            max_d = max([int(c) for c in (str(num))])
            if num > min(res[max_d]):
                temp = res[max_d] + [num]
                temp.sort()
                res[max_d] = temp[1:]
        temp = [sum(item) for item in res if 0 not in item]
        print(res)
        return max(temp) if temp != [] else -1
        
# @lc code=end

