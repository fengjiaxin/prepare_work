# 在英语中，我们有一个叫做 词根(root)的概念，它可以跟着其他一些词组成另一个较长的单词——我们称这个词为 继承词(successor)。例如，词根an，跟随着单词 other(其他)，可以形成新的单词 another(另一个)。
#
# 现在，给定一个由许多词根组成的词典和一个句子。你需要将句子中的所有继承词用词根替换掉。如果继承词有许多可以形成它的词根，则用最短的词根替换它。
#
# 你需要输出替换之后的句子。

# 需要注意的是如果word比trie中的短，那么都返回word

def replaceWords(dictionary, sentence):
    # 词根这个好理解，就是前向最短匹配
    class TNode:
        def __init__(self, val):
            self.val = val
            self.children = {}
            self.end = False

    class Trie:
        def __init__(self):
            self.root = TNode("")

        def insert(self, word):
            currNode = self.root
            for ch in word:
                if ch not in currNode.children:
                    currNode.children[ch] = TNode(ch)
                currNode = currNode.children[ch]
            currNode.end = True

        def shortPrefix(self, word):
            currNode = self.root
            length = len(word)
            for i in range(length):
                ch = word[i]
                if ch not in currNode.children:
                    return word
                else:
                    currNode = currNode.children[ch]
                    if currNode.end:
                        return word[:i + 1]
            return word

    trie = Trie()
    for d in dictionary:
        trie.insert(d)
    vec = sentence.split(" ")
    res = []
    for cv in vec:
        r = trie.shortPrefix(cv)
        res.append(r)
    return " ".join(res)

dicList = ["cat","bat","rat"]
sentence = "the c was rattled by the battery"
res = replaceWords(dicList, sentence)
print(res)