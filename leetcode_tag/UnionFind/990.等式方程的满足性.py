
# 给定一个由表示变量之间关系的字符串方程组成的数组，每个字符串方程 equations[i] 的长度为 4，并采用两种不同的形式之一："a==b" 或 "a!=b"。在这里，a 和 b 是小写字母（不一定不同），表示单字母变量名。
#
# 只有当可以将整数分配给变量名，以便满足所有给定的方程时才返回 true，否则返回 false。 

def equationsPossible(equations):
    # 思路：就是uf，如果相等的话，就将两个进行连通，如果不等，判断两个是否连通
    class UF:
        def __init__(self,n):
            self.total = n
            self.parent = [i for i in range(n)]
            self.size = [1 for i in range(n)]

        def find(self,x):
            while self.parent[x] != x:
                self.parent[x] = self.parent[self.parent[x]]
                x = self.parent[x]
            return x

        def isConnect(self,p,q):
            return self.find(p) == self.find(q)

        def union(self,p,q):
            rootp = self.find(p)
            rootq = self.find(q)
            if rootp == rootq:
                return
            rootp_size = self.size[rootp]
            rootq_size = self.size[rootq]
            if rootp_size > rootq_size:
                self.parent[rootq] = rootp
                self.size[rootp] += rootq_size
            else:
                self.parent[rootp] = rootq
                self.size[rootq] += rootp_size

    char2idx = {}
    connect = []
    unconnect = []
    for c in equations:
        first = c[0]
        second = c[3]
        if c[1] == "=":
            connect.append((first,second))
        else:
            unconnect.append((first,second))
        if first not in char2idx:
            char2idx[first] = len(char2idx)
        if second not in char2idx:
            char2idx[second] = len(char2idx)
    uf = UF(len(char2idx))
    for a,b in connect:
        a_idx = char2idx[a]
        b_idx = char2idx[b]
        uf.union(a_idx,b_idx)

    for a,b in unconnect:
        a_idx = char2idx[a]
        b_idx = char2idx[b]
        if uf.isConnect(a_idx,b_idx):
            return False
    return True

arr = ["a==b","b!=a"]
res = equationsPossible(arr)
print(res)