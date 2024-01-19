'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-02-11 16:06:04
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-02-11 17:20:07
FilePath: \Leetcode_Solver\22.括号生成.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        return self.generateParenthesisHelper(n,n,"",[])
    
    def generateParenthesisHelper(self, left, right,temp,res):
        
        # 结束条件
        if right == 0 or left == 0:
            if left == 0 :
                temp = temp + ")"*right

                res.append(temp)
            return res 
        elif left == 1 and right == 1:
            res.append(temp+"()")
            return res
        elif left == right:
            res += self.generateParenthesisHelper(left-1,right,temp+"(",res)
            return res
        elif left < right:
            res += self.generateParenthesisHelper(left-1,right,temp+"(",res)
            res += self.generateParenthesisHelper(left,right-1,temp+")",res)
            return res
        
        # 左括号比较多
        
           

       


        # if left >= right :
        #     res += self.generateParenthesisHelper(left-1,right,(current_stat),temp+"(",res)
        #     # if current_stat == True:
        #         res += self.generateParenthesisHelper(left,right-1,(not current_stat),temp+")",res)
        #     return res 
        
        # # 否则
        # if left < right :
     
        #     return res 
        
        
# @lc code=end

