class TNode:
    def __init__(self,val):
        self.val = val
        self.children = {}
        self.end = False

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TNode("")



    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        currNode = self.root
        for ch in word:
            if ch not in currNode.children:
                currNode.children[ch] = TNode(ch)
            currNode = currNode.children[ch]
        currNode.end = True



    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        currNode = self.root
        for ch in word:
            if ch not in currNode.children:
                return False
            currNode = currNode.children[ch]
        if not currNode.end:
            return False
        return True


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        currNode = self.root
        for ch in prefix:
            if ch not in currNode.children:
                return False
            currNode = currNode.children[ch]
        return True



word1 = "apple"
word2 = "app"
obj = Trie()
obj.insert(word1)
param_2 = obj.search(word1)
print(param_2)
param_3 = obj.startsWith(word2)
print(param_3)
obj.insert(word2)
param_4 = obj.search(word2)
print(param_4)