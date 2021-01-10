
# 输入一个图，该图由一个有着N个节点 (节点值不重复1, 2, ..., N) 的树及一条附加的边构成。附加的边的两个顶点包含在1到N中间，这条附加的边不属于树中已存在的边。
#
# 结果图是一个以边组成的二维数组。每一个边的元素是一对[u, v] ，满足 u < v，表示连接顶点u 和v的无向图的边。
#
# 返回一条可以删去的边，使得结果图是一个有着N个节点的树。如果有多个答案，则返回二维数组中最后出现的边。答案边 [u, v] 应满足相同的格式 u < v。

def findRedundantConnection(edges):
    class UF:
        def __init__(self, n):
            self.parent = [i for i in range(n)]

        def find(self, x):
            while self.parent[x] != x:
                self.parent[x] = self.parent[self.parent[x]]
                x = self.parent[x]
            return x

        def union(self, p, q):
            rootp = self.find(p)
            rootq = self.find(q)
            if rootp == rootq:
                return
            self.parent[rootq] = rootp

        def isConnected(self, p, q):
            rootp = self.find(p)
            rootq = self.find(q)
            return rootp == rootq

    city2id = {}
    for edge in edges:
        for c in edge:
            if c not in city2id:
                city2id[c] = len(city2id)
    uf = UF(len(city2id))
    for edge in edges:
        a_id = city2id[edge[0]]
        b_id = city2id[edge[1]]
        if uf.isConnected(a_id, b_id):
            return edge
        else:
            uf.union(a_id, b_id)

egs = [[1,2], [2,3], [3,4], [1,4], [1,5]]
edge = findRedundantConnection(egs)
print(edge)