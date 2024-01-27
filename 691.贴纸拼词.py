#
# @lc app=leetcode.cn id=691 lang=python3
#
# [691] 贴纸拼词
#
from collections import Counter
# @lc code=start
class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        
        alphabet = "abcdefghigklmnopqrstuvwxyz"
        
        total, have, require = Counter(), {}, Counter(target)
        for s in stickers:
            have[s] = Counter(s)
            total += Counter(s)
        
        for s in require:
            if s not in total:
                return False

        
        
        
        
# @lc code=end

