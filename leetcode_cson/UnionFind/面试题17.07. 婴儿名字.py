
# 每年，政府都会公布一万个最常见的婴儿名字和它们出现的频率，也就是同名婴儿的数量。有些名字有多种拼法，例如，John 和 Jon 本质上是相同的名字，但被当成了两个名字公布出来。给定两个列表，一个是名字及对应的频率，另一个是本质相同的名字对。设计一个算法打印出每个真实名字的实际频率。注意，如果 John 和 Jon 是相同的，并且 Jon 和 Johnny 相同，则 John 与 Johnny 也相同，即它们有传递和对称性。
#
# 在结果列表中，选择字典序最小的名字作为真实名字。

# 分析，特别绕口，核心思想还是把名字进行连通，可以通过parentId确认相同的范围，然后从相同的范围中找到新的parent名字

# 很绕啊
import collections
def trulyMostPopular(names, synonyms):
    # 首先要做的就是对每个名称编码
    name2id = {}
    name2freq = {}
    for namef in names:
        vec = namef.split("(")
        name = vec[0]
        freq = int(vec[1][:-1])
        name2id[name] = len(name2id)
        name2freq[name] = freq
    for syss in synonyms:
        vec = syss.split(",")
        a_name = vec[0][1:]
        b_name = vec[1][:-1]
        for name in [a_name, b_name]:
            if name not in name2id:
                name2id[name] = len(name2id)
                name2freq[name] = 0
    id2name = {}
    for name, idx in name2id.items():
        id2name[idx] = name
    parent = [i for i in range(len(id2name))]

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for syss in synonyms:
        vec = syss.split(",")
        a_name = vec[0][1:]
        b_name = vec[1][:-1]
        a_id = name2id[a_name]
        b_id = name2id[b_name]
        roota = find(a_id)
        rootb = find(b_id)
        if roota == rootb:
            continue
        parent[rootb] = roota
    # 存储parentId 和 children name的对应关系
    ans = collections.defaultdict(list)
    # 存储parentId 和 freq的对应关系
    freq = collections.defaultdict(int)
    for i in range(len(id2name)):
        parent_i = find(i)
        ans[parent_i].append(id2name[i])
        freq[parent_i] += name2freq[id2name[i]]
    res = []
    for pid, ls in ans.items():
        if freq[pid] == 0:
            continue
        ls.sort()
        s = ls[0] + "(" + str(freq[pid]) + ")"
        res.append(s)
    return res


names = ["John(15)","Jon(12)","Chris(13)","Kris(4)","Christopher(19)"]
synonyms = ["(Jon,John)","(John,Johnny)","(Chris,Kris)","(Chris,Christopher)"]
res = trulyMostPopular(names, synonyms)
print(res)