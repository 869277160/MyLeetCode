#
# @lc app=leetcode.cn id=1560 lang=python3
#
# [1560] 圆形赛道上经过次数最多的扇区
#

# @lc code=start
class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        
        # res = [0 for i in range(n+1)]
        # res[rounds[0]]+=1
        
        # for j in range(len(rounds)-1):
        #     if rounds[j] < rounds[j+1]:
        #         for i in range(rounds[j]+1,rounds[j+1]+1):
        #             res[i] += 1
        #     else:
        #         for i in range(rounds[j]+1,n+1):
        #             res[i] += 1
                
        #         for i in range(1,rounds[j+1]+1):
        #             res[i] += 1
                
        #     print(res)
        
        # max_pos = []
        # for i in range(len(res)):
        #     if res[i] == max(res):
        #         max_pos.append(i)
        
        # return max_pos
        
        
        
        s, e = rounds[0], rounds[-1]
        if s <= e:
            # [起点, 终点]
            return list(range(s, e + 1))
        else:
            # [1, 终点]+[起点, n]
            return list(range(1, e + 1)) + list(range(s, n + 1))
# @lc code=end

