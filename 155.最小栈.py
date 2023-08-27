#
# @lc app=leetcode.cn id=155 lang=python3
#
# [155] 最小栈
#

# @lc code=start
class MinStack:

    def __init__(self):
        
        self.input_stack = list()
        self.min_stack = list()
        self.current_min = float('inf')

    def push(self, val: int) -> None:
        self.input_stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            # 新插入的这个元素就是全栈最小的
            self.min_stack.append(val)
        else:
            # 插入的这个元素比较大
            self.min_stack.append(self.min_stack[-1])
            

    def pop(self) -> None:
        self.input_stack.pop()
        self.min_stack.pop()
        
        
    def top(self) -> int:
        # None is for empty stack.
        return self.input_stack[-1]
    
    def getMin(self) -> int:
        # None is for empty stack.
        return self.min_stack[-1]  


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

