#
# @lc app=leetcode.cn id=1189 lang=python3
#
# [1189] “气球” 的最大数量
#

# @lc code=start
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
       
        
        import collections
        text_dict = collections.Counter(text)
        
        all_counter = [
            text_dict["b"],
            text_dict["a"],
            text_dict["n"],
            text_dict["l"]//2,
            text_dict["o"]//2,
        ]
        
        return min(all_counter)
        
        
        
# @lc code=end

