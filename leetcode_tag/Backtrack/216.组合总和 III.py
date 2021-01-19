# 找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。
#
# 说明：
#
# 所有数字都是正整数。
# 解集不能包含重复的组合。 

class Solution:
    def combinationSum3(self, k, n):
        res = []
        # 已经的路径path,遗留的left_sum,start是1-9
        def helper(path,left_sum,start):
            if len(path) == k:
                if left_sum == 0:
                    res.append(path.copy())
                return

            for i in range(start,10):
                if i > left_sum:
                    break
                path.append(i)
                helper(path,left_sum - i,i+1)
                path.pop(-1)
        helper([],n,1)
        return res

k = 3
n = 7
s = Solution()
res = s.combinationSum3(k,n)
print(res)