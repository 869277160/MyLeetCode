#
# @lc app=leetcode.cn id=1128 lang=python3
#
# [1128] 等价多米诺骨牌对的数量
#

# @lc code=start
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        
        dominoes2nums= [10*max(domino[0],domino[1])+min(domino[0],domino[1]) for domino in dominoes]
        
        # 进一步改进，改为可hash值后使用计数器
        import collections
        freq = collections.Counter(dominoes2nums)
        
        count = 0
        for key in freq.keys():
            freq[key] -= 1 
            count += freq[key]*(freq[key]+1)//2

        print(freq)
        
        print(count)
        return count 
        
        # 改进的暴力求解，带备忘录
        # domino_set = []
        # domino_sumer = [0 for i in dominoes]

        # for i in range(0,len(dominoes)):
        #     if dominoes[i] not in domino_set:
        #         domino_set.append(dominoes[i])
        #         domino_set.append([dominoes[i][1],dominoes[i][0]])
        #         domino_sumer[i] = dominoes.count(dominoes[i])  -1 
        #         if dominoes[i][0] != dominoes[i][1]:
        #             domino_sumer[i] += dominoes.count([dominoes[i][1],dominoes[i][0]])
                
        #         if domino_sumer[i] !=0 :
        #             temp_count = domino_sumer[i]-1
        #             for j in range(i+1,len(dominoes)):
        #                 if self.sameDomio(dominoes[j],dominoes[i]):
        #                     domino_sumer[j] = temp_count
        #                     temp_count = temp_count -1  
        # # print(domino_sumer)
        
        # return sum(domino_sumer)
                             
        
        
        # 暴力求解，两次遍历
        # count = 0
        # for i in range(len(dominoes)):
        #     for j in range(i+1,len(dominoes)):
        #         if self.sameDomio(dominoes[i],dominoes[j]):
        #             count +=1 
        
        # return count
        
    def sameDomio(self, a, b):
        if a == b or (a[1] == b[0] and a[0] == b[1]):
            return True
        else:
            return False
# @lc code=end

