#
# @lc app=leetcode.cn id=3005 lang=python3
#
# [3005] 最大频率元素计数
#

# @lc code=start
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        
        from collections import Counter
        
        n_count = Counter(nums)
        max_freq = n_count.most_common(1)[0][1]
        res = 0 
        for num in n_count:
             if n_count[num] == max_freq:
                 res += max_freq
        return res
        
# @lc code=end

