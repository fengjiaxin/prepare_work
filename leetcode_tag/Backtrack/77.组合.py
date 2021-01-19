# 给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

class Solution:
    def combine(self, n, k):
        res = []
        def helper(path,start):
            if len(path) == k:
                res.append(path.copy())
                return
            if start > n:
                return
            for i in range(start,n+1):
                path.append(i)
                helper(path,i+1)
                path.pop(-1)
        helper([],1)
        return res

n = 4
k = 2
s = Solution()
res = s.combine(n,k)
print(res)