
# 有 n 个城市，其中一些彼此相连，另一些没有相连。如果城市 a 与城市 b 直接相连，且城市 b 与城市 c 直接相连，那么城市 a 与城市 c 间接相连。
# 省份 是一组直接或间接相连的城市，组内不含其他没有相连的城市。
# 给你一个 n x n 的矩阵 isConnected ，其中 isConnected[i][j] = 1 表示第 i 个城市和第 j 个城市直接相连，而 isConnected[i][j] = 0 表示二者不直接相连。
# 返回矩阵中 省份 的数量。


def findCircleNum(isConnected):
    # 这就是一个uf问题
    class UF:
        def __init__(self,n):
            self.num = n
            self.parent = [i for i in range(n)]

        def find(self,x):
            while self.parent[x] != x:
                self.parent[x] = self.parent[self.parent[x]]
                x = self.parent[x]
            return x

        def union(self,p,q):
            rootP = self.find(p)
            rootQ = self.find(q)
            if rootP == rootQ:
                return
            self.parent[rootQ] = rootP
            self.num -= 1

    city_num = len(isConnected)
    uf = UF(city_num)
    for i in range(city_num):
        for j in range(i):
            if isConnected[i][j] == 1:
                uf.union(i,j)
    return uf.num

arr = [[1,1,0],[1,1,0],[0,0,1]]
res = findCircleNum(arr)
print(res)