# 设计一个使用单词列表进行初始化的数据结构，单词列表中的单词 互不相同 。 如果给出一个单词，请判定能否只将这个单词中一个字母换成另一个字母，使得所形成的新单词存在于你构建的字典中。
#
# 实现 MagicDictionary 类：
#
# MagicDictionary() 初始化对象
# void buildDict(String[] dictionary) 使用字符串数组 dictionary 设定该数据结构，dictionary 中的字符串互不相同
# bool search(String searchWord) 给定一个字符串 searchWord ，判定能否只将字符串中 一个 字母换成另一个字母，使得所形成的新字符串能够与字典中的任一字符串匹配。如果可以，返回 true ；否则，返回 false 。

# 思路：在匹配的时候需要注意不能和原来的单词完全一样

class TNode:
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.end = False


class MagicDictionary:
    # 思想：判断是否能将其中一个字符替换成另一个字符和字典中的任意字符匹配，说白了就是将某个字符变成.进行搜索

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TNode("")

    def addWord(self, word):
        currNode = self.root
        for ch in word:
            if ch not in currNode.children:
                currNode.children[ch] = TNode(ch)
            currNode = currNode.children[ch]
        currNode.end = True

    def buildDict(self, dictList):
        """
        Build a dictionary through a list of words
        """
        for word in dictList:
            self.addWord(word)

    def find(self, word, i, num, node):
        # 查找word的第i个字符开始，num为还可以替换的次数
        if num < 0:
            return False
        if i == len(word):
            return num == 0 and node.end
        ch = word[i]
        for pre in node.children:
            if pre == ch:
                if self.find(word, i + 1, num, node.children[ch]):
                    return True
            else:
                if self.find(word, i + 1, num - 1, node.children[pre]):
                    return True
        return False

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        """
        return self.find(word, 0, 1, self.root)

# Your MagicDictionary object will be instantiated and called as such:
obj = MagicDictionary()
obj.buildDict(["hello", "leetcode"])
param_1 = obj.search("hello")
param_2 = obj.search("hhllo")
param_3 = obj.search("hell")
param_4 = obj.search("leetcoded")
print(param_1)
print(param_2)
print(param_3)
print(param_4)