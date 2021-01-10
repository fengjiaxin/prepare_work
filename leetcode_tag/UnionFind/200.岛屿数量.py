# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
#
# 岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
#
# 此外，你可以假设该网格的四条边均被水包围。
#
#
# 示例 1：
#
# 输入：grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# 输出：1

def numIslands(grid):
    # 并查集
    class UF:
        def __init__(self, n):
            self.n = n
            self.parent = [i for i in range(n)]

        def find(self, x):
            while self.parent[x] != x:
                self.parent[x] = self.parent[self.parent[x]]
                x = self.parent[x]
            return x

        def union(self, p, q):
            rootp = self.find(p)
            rootq = self.find(q)
            if rootp != rootq:
                self.parent[rootq] = rootp
                self.n -= 1

    m = len(grid)
    n = len(grid[0])
    # 先统计一下1的个数
    loc2id = {}
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "1":
                loc2id[(i, j)] = len(loc2id)
    uf = UF(len(loc2id))
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "1":
                for a, b in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    next_i = i + a
                    next_j = j + b
                    if 0 <= next_i and next_i < m and 0 <= next_j and next_j < n and grid[next_i][next_j] == "1":
                        uf.union(loc2id[(i, j)], loc2id[(next_i, next_j)])
    return uf.n

grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
res = numIslands(grid)
print(res)