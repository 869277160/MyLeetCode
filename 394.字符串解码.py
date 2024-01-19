#
# @lc app=leetcode.cn id=394 lang=python3
#
# [394] 字符串解码
#

# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        
        
        stack, res, multi = [], "", 0
        for c in s:
            if c == '[':
                stack.append([multi, res])
                res, multi = "", 0
            elif c == ']':
                cur_multi, last_res = stack.pop()
                res = last_res + cur_multi * res
            elif '0' <= c <= '9':
                multi = multi * 10 + int(c)
            else:
                res += c
        return res


        
        def findlast(s,start):
            count = 1
            for i in range(start+1,len(s)):
                if s[i] == '[':
                    count += 1
                elif s[i] == ']':
                    count -= 1
                    if count == 0:
                        return i 

            return len(s)
        
        # def repeat(inputpart, times):
        #     # 考虑循环嵌套的情况
        #     if "[" not in inputpart and "]" not in inputpart:
        #         return inputpart * times
        #     else:
        #         res = ""
            
        #     return res 
        
        current = s
        while(current.count("[") > 0):

            current_pos = 0
            # 每次只处理最浅一层的括号
            while(current_pos < len(s)):
                if s[current_pos].isdigit():
                    start,end = current_pos+2, findlast(s,current_pos+1)
                    single_word = s[start:end]
                    if "[" not in single_word and "]" not in single_word:
                        if current_pos == 0:
                            current = single_word * int(s[current_pos]) + s[end+1:]
                        else :
                            current = current[:current_pos] + single_word * int(s[current_pos]) + s[end+1:]
                        current_pos = end + 1
                    else :
                        current_pos +=1 
                else:
                    current_pos += 1
            print(current)
        
        return current
                    
                    
            
        
        
        
        
# @lc code=end

