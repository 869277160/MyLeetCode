'''
Author: wangding wangding19@mails.ucas.ac.cn
Date: 2023-03-10 16:31:15
LastEditors: wangding wangding19@mails.ucas.ac.cn
LastEditTime: 2023-03-10 16:32:10
FilePath: \Leetcode_Solver\195.第十行.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''

# awk 'NR == 10' file.txt NR在awk中指行号

# file.txt -n表示只输出匹配行，p表示Print

sed -n 10p 

# tail -n+10 file.txt|head -1 tail -n +10表示从第10行开始输出