'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-20 09:48:38
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-20 20:10:45
FilePath: \Leetcode_Solver\953.验证外星语词典.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=953 lang=python3
#
# [953] 验证外星语词典
#

# @lc code=start
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        
        
        order_dict = {order[i]:i for i in range(len(order))}
        
        
        return words == sorted(words, key=lambda x: [order_dict[c] for c in x])
        
        
        # for i in range(len(words)-1):
        #     total_len = min(len(words[i]),len(words[i+1]))
            
        #     for j in range(total_len):
        #         if words[i][j] != words[i+1][j]:
        #             if order_dict[words[i][j]] > order_dict[words[i+1][j]]:
        #                 return False
        #             else:
        #                 pass
          
        #     if len(words[i]) > len(words[i+1]) and words[i][:total_len] == words[i+1]:
        #         return False
        
        # return True
                
                
        
        
        # # check length 
        # length = [len(word) for word in words]
        # for i in range(len(length)-1):
        #     if length[i] > length[i+1]:
        #         return False
        
        # # check order
        # for i in range(len(words)-1):
        #     for j in range(len(words[i])):
        #         if words[i][j] != words[i+1][j]:
        #             if order.index(words[i][j]) > order.index(words[i+1][j]):
        #                 return False
        #             else:
        #                 break
        
        # return True
        
# @lc code=end

