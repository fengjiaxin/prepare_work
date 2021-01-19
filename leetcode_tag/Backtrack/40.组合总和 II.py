# 给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
#
# candidates 中的每个数字在每个组合中只能使用一次。
#
# 说明：
#
# 所有数字（包括目标数）都是正整数。
# 解集不能包含重复的组合。 

class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        res = []
        length = len(candidates)
        # first表示选择范围在[first:]
        def helper(path,left_sum,first):
            if left_sum == 0:
                res.append(path.copy())
                return
            else:
                for i in range(first,length):
                    ca = candidates[i]
                    if ca > left_sum:
                        break
                    if i > first and candidates[i] == candidates[i-1]:
                        continue

                    path.append(ca)
                    helper(path,left_sum - ca,i+1)
                    path.pop(-1)
        helper([],target,0)
        return res

candidates =  [10,1,2,7,6,1,5]
target = 8
s = Solution()
res = s.combinationSum2(candidates,target)
print(res)