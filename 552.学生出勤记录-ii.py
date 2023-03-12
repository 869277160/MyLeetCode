'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-16 22:25:29
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-17 10:29:21
FilePath: \Leetcode_Solver\552.学生出勤记录-ii.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=552 lang=python3
#
# [552] 学生出勤记录 II
#

# @lc code=start
class Solution:
    def checkRecord(self, n: int) -> int:
        if n == 1 :
            return 3
#         # if n == 2 :
#         #     return 8
#         # if n == 3 :
#         #     return 19
        
        # res = []
        # for i in range(n+1):
        #     res.append([0,0,0])
        # res[1] = [1,1,1]
        # res[2] = [3,2,3]
        # res[3] = [8,6,6]
        
        # # last = "P"
        # for i in range(1,n+1):
        #     if i == 1:
        #         self.res[i][0] = 1
        #         self.res[i][1] = 1
        #         self.res[i][2] = 1
        #     else:
        #         self.res[i][0] = (self.res[i-1][0] + self.res[i-1][1] + self.res[i-1][2]) % 1000000007
                
        #         self.res[i][1] = (self.res[i-1][0] + self.res[i-1][2]) % 1000000007
                
        #         self.res[i][2] = (self.res[i-1][0] + self.res[i-1][1] + (self.res[i-1][2] - self.res[i-2][2]) +  self.res[i-2][0] + self.res[i-2][1]) % 1000000007

        # return sum(self.res[n]) % 1000000007
        return (self.helper(n-1,A_state=0,L_state=0)) % 1000000007 + (self.helper(n-1,A_state=1,L_state=0)) % 1000000007 + (self.helper(n-1,A_state=0,L_state=1)) % 1000000007
    
    def helper(self,n,A_state,L_state):
        #  end of loop
        if n == 1:
            if A_state == 1:
                return 2 
            else:
                if L_state == 2:
                    return 2
                else :
                    return 3
        else:
            if A_state == 1:
                if L_state == 2:
                    return (self.helper(n-1,A_state=1,L_state=2)  ) % 1000000007
                else:
                    return (self.helper(n-1,A_state=1,L_state=L_state+1) + self.helper(n-1,A_state=1,L_state=L_state+1)) % 1000000007

            else :
                if L_state == 2:
                    return (self.helper(n-1,A_state=0,L_state=2) + self.helper(n-1,A_state=1,L_state=2) ) % 1000000007
                else :
                    return (self.helper(n-1,A_state=0,L_state=L_state)) % 1000000007 + (self.helper(n-1,A_state=1,L_state=L_state)) % 1000000007 + (self.helper(n-1,A_state=0,L_state=L_state+1)) % 1000000007

                
            # elif A_state == 1 and L_state == 1:
            #     return (self.helper(n-1,"P") + self.helper(n-1,"A") + self.helper(n-1,"LL")) % 1000000007
            # elif last == "LL":
            #     return (self.helper(n-1,"P") + self.helper(n-1,"A") ) % 1000000007
            # else:
            #     return (self.helper(n-1,"P") + self.helper(n-1,"A") + self.helper(n-1,"L")) % 1000000007
        
        
        
        
# @lc code=end

