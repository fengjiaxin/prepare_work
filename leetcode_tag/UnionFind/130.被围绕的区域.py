# 给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。
#
# 找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。
#
# 示例:
#
# X X X X
# X O O X
# X X O X
# X O X X
# 运行你的函数后，矩阵变为：
#
# X X X X
# X X X X
# X X X X
# X O X X
# 解释:
#
# 被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。

def solve(board):
    """
    Do not return anything, modify board in-place instead.
    """
    # 如何运用union find呢？
    # 1.首先将O进行连通，然后遍历边上的O,如果一堆中有边上的O，这一堆就不要留着
    if len(board) == 0: return
    m = len(board)
    n = len(board[0])
    loc2id = {}
    for i in range(m):
        for j in range(n):
            if board[i][j] == "O":
                loc2id[(i, j)] = len(loc2id)

    parent = [i for i in range(len(loc2id))]

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(p, q):
        rootp = find(p)
        rootq = find(q)
        if rootp != rootq:
            parent[rootq] = rootp

    for i in range(m):
        for j in range(n):
            if board[i][j] == "O":
                for a, b in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    next_i = i + a
                    next_j = j + b
                    if 0 <= next_i and next_i < m and 0 <= next_j and next_j < n and board[next_i][next_j] == "O":
                        union(loc2id[(i, j)], loc2id[(next_i, next_j)])
    ans = collections.defaultdict(list)
    id2loc = {}
    for k, v in loc2id.items():
        id2loc[v] = k
    for i in range(len(loc2id)):
        parent_i = find(i)
        ans[parent_i].append(i)

    # 需要变成x的id
    needIdx = []

    def isInOutline(l):
        for idx in l:
            i, j = id2loc[idx]
            if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                return True
        return False

    for l in ans.values():
        if not isInOutline(l):
            needIdx.extend(l)
    for idx in needIdx:
        i, j = id2loc[idx]
        board[i][j] = "X"

