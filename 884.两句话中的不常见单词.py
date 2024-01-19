#
# @lc app=leetcode.cn id=884 lang=python3
#
# [884] 两句话中的不常见单词
#

# @lc code=start
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words1 =s1.split()
        words2 =s2.split()
        
        worddict1 = {}
        worddict2 = {}
            
        res= []
        for word in words1:
            if word in worddict1.keys():
                if word in res :
                    res.remove(word)
                worddict1[word] +=1
            else :
                if word not in words2:
                    res.append(word)
                    worddict1[word] = 1
                else:
                    worddict2[word] = 1
                    worddict1[word] = 1

        for word in words2:
            if word not in worddict2.keys():
                res.append(word)
                worddict2[word] =1
            else:
                if word in res :
                    res.remove(word)
                worddict2[word] +=1
                

        
        return res
        
# @lc code=end

