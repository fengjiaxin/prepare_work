# 实现一个 MapSum 类，支持两个方法，insert 和 sum：
#
# MapSum() 初始化 MapSum 对象
# void insert(String key, int val) 插入 key-val 键值对，字符串表示键 key ，整数表示值 val 。如果键 key 已经存在，那么原来的键值对将被替代成新的键值对。
# int sum(string prefix) 返回所有以该前缀 prefix 开头的键 key 的值的总和。

# 前缀和这种问题，使用递归，但是需要注意递归的边界条件

class TNode:
    def __init__(self, val):
        self.val = val
        self.weight = 0
        self.end = False
        self.children = {}

class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TNode("")

    def insert(self, key, val):
        currNode = self.root
        for ch in key:
            if ch not in currNode.children:
                currNode.children[ch] = TNode(ch)
            currNode = currNode.children[ch]
        currNode.weight = val
        currNode.end = True

    # 不包含startNode.weight
    def sum_help(self, startNode):
        if len(startNode.children) == 0:
            return 0
        res = 0
        for ch in startNode.children:
            nextNode = startNode.children[ch]
            if nextNode.end:
                res += nextNode.weight
            res += self.sum_help(nextNode)
        return res

    def sum(self, prefix):
        currNode = self.root
        for ch in prefix:
            if ch not in currNode.children:
                return 0
            currNode = currNode.children[ch]

        return self.sum_help(currNode) + currNode.weight

# Your MapSum object will be instantiated and called as such:
obj = MapSum()
obj.insert("apple",3)
param_1 = obj.sum("ap")
obj.insert("app",2)
param_2 = obj.sum("ap")
print(param_1)
print(param_2)