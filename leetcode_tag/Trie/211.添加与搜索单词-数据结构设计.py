# 请你设计一个数据结构，支持 添加新单词 和 查找字符串是否与任何先前添加的字符串匹配 。
#
# 实现词典类 WordDictionary ：
#
# WordDictionary() 初始化词典对象
# void addWord(word) 将 word 添加到数据结构中，之后可以对它进行匹配
# bool search(word) 如果数据结构中存在字符串与 word 匹配，则返回 true ；否则，返回  false 。word 中可能包含一些 '.' ，每个 . 都可以表示任何一个字母。

class TNode:
    def __init__(self,val):
        self.val = val
        self.children = {}
        self.end = False


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TNode("")


    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        currNode = self.root
        for ch in word:
            if ch not in currNode.children:
                currNode.children[ch] = TNode(ch)
            currNode = currNode.children[ch]
        currNode.end = True


    def baseSearch(self,startNode,word,idx):
        if idx == len(word):
            return startNode.end
        ch = word[idx]
        if ch == ".":
            for prefix in startNode.children:
                if self.baseSearch(startNode.children[prefix],word,idx+1):
                    return True
            return False
        else:
            if ch not in startNode.children:
                return False
            return self.baseSearch(startNode.children[ch],word,idx+1)



    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        return self.baseSearch(self.root,word,0)




# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
obj.addWord("bad")
obj.addWord("dad")
obj.addWord("mad")
param_2 = obj.search("pad")
param_3 = obj.search("bad")
param_4 = obj.search(".ad")
param_5 = obj.search("b..")
print(param_2)
print(param_3)
print(param_4)
print(param_5)