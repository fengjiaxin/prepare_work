# 给你一个字符串 s，以及该字符串中的一些「索引对」数组 pairs，其中 pairs[i] = [a, b] 表示字符串中的两个索引（编号从 0 开始）。
#
# 你可以 任意多次交换 在 pairs 中任意一对索引处的字符。
#
# 返回在经过若干次交换后，s 可以变成的按字典序最小的字符串。
#
#  
#
# 示例 1:
#
# 输入：s = "dcab", pairs = [[0,3],[1,2]]
# 输出："bacd"
# 解释：
# 交换 s[0] 和 s[3], s = "bcad"
# 交换 s[1] 和 s[2], s = "bacd"

# 听着很绕，其实就是保证连通的index的集合中位置保持是有序的即可，比如1，3，5连通，那么保证1，3，5位置处组合的字符字典序最小即可
import collections
def smallestStringWithSwaps(s, pairs):
    # 思路：首先确定哪些index是连通的，然后保证连通的index是有序的即可
    length = len(s)
    p = [i for i in range(length)]

    def find(x):
        while x != p[x]:
            p[x] = p[p[x]]
            x = p[x]
        return x

    # 合并结束
    for pair in pairs:
        a_id = pair[0]
        b_id = pair[1]
        roota = find(a_id)
        rootb = find(b_id)
        if roota == rootb:
            continue
        p[rootb] = roota
    # key是parent_id,value是连通index的集合
    ans = collections.defaultdict(list)
    for i in range(length):
        parent_i = find(i)
        ans[parent_i].append(i)
    res = list(s)
    for same_idxs in ans.values():
        same_idxs.sort()
        selectStr = [s[i] for i in same_idxs]
        selectStr.sort()
        for i, idx in enumerate(same_idxs):
            res[idx] = selectStr[i]
    return "".join(res)

s = "dcab"
pairs = [[0,3],[1,2]]

res = smallestStringWithSwaps(s, pairs)
print(res)