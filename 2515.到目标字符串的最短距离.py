#
# @lc app=leetcode.cn id=2515 lang=python3
#
# [2515] 到目标字符串的最短距离
#

# @lc code=start
class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        
        total_len = len(words)
        
        if  target not in words:
            return -1 
        else:
            if words.count(target) == 1:
               
                dist1 = abs(words.index(target) - startIndex )
                dist2 = total_len - dist1
                
                dist = min(dist1,dist2)
                
                return dist
            
            else:
                triple_words = words + words + words
                for i in range(0,len(words)+1):
                    # if startIndex - i >= 0 :
                        print(triple_words[startIndex - i], startIndex - i)
                        if triple_words[startIndex+total_len - i] == target:
                            return i
                    
                    # if startIndex + i < len(words)*2:
                        print(triple_words[startIndex + i],startIndex + i)
                        if triple_words[startIndex+ total_len + i] == target:
                            return i
                        
 
# @lc code=end

