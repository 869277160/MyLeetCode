#
# @lc app=leetcode.cn id=1832 lang=python3
#
# [1832] 判断句子是否为全字母句
#

# @lc code=start
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:

        s_dict = {}
        for i in sentence:
            if i not in s_dict:
                s_dict[i]= 0
            s_dict[i]+=1

        return len(s_dict.keys()) == 26
        
        
# @lc code=end

