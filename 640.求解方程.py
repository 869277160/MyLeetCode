'''
Author: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
Date: 2023-02-07 10:18:40
LastEditors: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
LastEditTime: 2023-02-07 11:08:16
FilePath: \Leetcode_Solver\640.求解方程.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
#
# @lc app=leetcode.cn id=640 lang=python3
#
# [640] 求解方程
#

# @lc code=start
class Solution:
    # 思路清晰的大型题目一定要注意模块化。
    # 同时注意输入case 是否会有空。
    def solveEquation(self, equation: str) -> str:

        left,right = equation.split("=")

        left_dict = self.PartChecker(left)
        right_dict = self.PartChecker(right)

        if right_dict["x"] == left_dict["x"] and right_dict["nums"] == left_dict["nums"]:
            return "Infinite solutions"
        
        x =  left_dict["x"] - right_dict["x"]
        num = right_dict["nums"] - left_dict["nums"] 
        
        if (x == 0):
            return "No solution"
        if num % x != 0:
            return "No solution"
        
        res= num // x
        return f"x={res}"
            
    
    def PartChecker(self,left):
        res_dict = {"x":0,"nums":0}
        
        left_part = left.split("+")
        for item in left_part:
            # 没有减号
            if item.find("-") == -1:
               item_dict = self.itemChecker(item,op=1)
               res_dict["x"] += item_dict["x"]
               res_dict["nums"] += item_dict["nums"]
               
            # 有减号
            else:
                minus_part = item.split("-")
                if minus_part[0] != "":
                    item_dict = self.itemChecker(minus_part[0],op=1)
                    res_dict["x"] += item_dict["x"]
                    res_dict["nums"] += item_dict["nums"]
                
                # 处理其余项
                for i in range(1,len(minus_part)):
                    item_dict = self.itemChecker(minus_part[i],op=-1)
                    res_dict["x"] += item_dict["x"]
                    res_dict["nums"] += item_dict["nums"]
        return res_dict 
        
        
    def itemChecker(self,item,op=1):
        res_dict = {"x":0,"nums":0}
        if item == "":
            return res_dict
            
        # x项
        if item.find("x") != -1:
            if len(item)!=1:
                res_dict["x"] += (int(item.split('x')[0]) *op)
            else :
                res_dict["x"] += (1*op)
        # 数字项
        else:
            res_dict["nums"] += (int(item)*op)
            
        return res_dict 
        
# @lc code=end

