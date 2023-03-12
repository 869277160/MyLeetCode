#
# @lc app=leetcode.cn id=1002 lang=python3
#
# [1002] 查找共用字符
#

# @lc code=start
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        all_letter = [set(i) for i in words]
        
        res = []
        for i in range(len(res)):
            for j in range(i+1,len(res)):
                if res[i] in res[j]:
                    res.append(res[i])
        
        
        return list()
        
# @lc code=end

