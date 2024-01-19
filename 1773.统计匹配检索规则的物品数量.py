#
# @lc app=leetcode.cn id=1773 lang=python3
#
# [1773] 统计匹配检索规则的物品数量
#

# @lc code=start
class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        
        ruleKey_list = []
        if ruleKey == "type":
            ruleKey_list = [item[0] for item in items]
        if ruleKey == "color":
            ruleKey_list = [item[1] for item in items]
        if ruleKey == "name":
            ruleKey_list = [item[2] for item in items]
        
        import collections
        freq = collections.Counter(ruleKey_list)
        
        return freq[ruleValue]
        
        
        
        
# @lc code=end

