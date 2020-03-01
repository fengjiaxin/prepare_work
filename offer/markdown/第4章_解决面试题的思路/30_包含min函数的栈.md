### 面试题30:包含min函数的栈

&emsp;题目：定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的min函数，在该栈中，调用min,push，pop的时间复杂度都是O(1)

&emsp;**思路**:能够在O(1)的时间复杂度内得到栈的最小元素，那么需要一个辅助栈，该辅助栈存储的是该栈中的最小元素，那么假设栈是空，直接加入到栈中，如果新来的元素比最小元素栈顶小，那么需要将该值加入到辅助栈中，如果新来的元素比最小元素栈顶大，那么将栈顶元素复制加入到辅助栈中，这样就维护了一个辅助栈，在O(1)时间内得到最小函数


```python
class Solution:
    def __init__(self):
        self.data_stack = []
        self.min_stack = []
    def push(self, node):
        # write code here
        if not self.data_stack:
            self.data_stack.append(node)
            self.min_stack.append(node)
        elif self.data_stack:
            curr_min = self.min_stack[-1]
            if node <= curr_min:
                self.min_stack.append(node)
            elif node > curr_min:
                self.min_stack.append(self.min_stack[-1])
            self.data_stack.append(node)
    def pop(self):
        # write code here
        self.min_stack.pop(-1)
        return self.data_stack.pop(-1)
    def top(self):
        # write code here
        return self.data_stack[-1]
    def min(self):
        # write code here
        return self.min_stack[-1]
```
