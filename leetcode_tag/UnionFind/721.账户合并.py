# 给定一个列表 accounts，每个元素 accounts[i] 是一个字符串列表，其中第一个元素 accounts[i][0] 是 名称 (name)，其余元素是 emails 表示该账户的邮箱地址。
#
# 现在，我们想合并这些账户。如果两个账户都有一些共同的邮箱地址，则两个账户必定属于同一个人。请注意，即使两个账户具有相同的名称，它们也可能属于不同的人，因为人们可能具有相同的名称。一个人最初可以拥有任意数量的账户，但其所有账户都具有相同的名称。
#
# 合并账户后，按以下格式返回账户：每个账户的第一个元素是名称，其余元素是按顺序排列的邮箱地址。账户本身可以以任意顺序返回。

# 这道题很绕
# 思路:肯定是并查集，在合并的时候，注意是p的父节点指向q的父节点
import collections
def accountsMerge(accounts):
    class UF:
        def __init__(self,n):
            self.parent = [i for i in range(n)]
            self.num = n

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


    # 分析题意：有个限制，一个人最初可以有任意数量的账户，但是账户都具有相同的名称,所以不存在同一个email对应不同的名称
    email2name = {}
    email2id = {}

    # 最多1000个账户，每个账户最多9个邮箱，那一共最多9000个emails
    uf = UF(9000)

    for account in accounts:
        name = account[0]
        emails = account[1:]
        for email in emails:
            if email not in email2name:
                email2name[email] = name
                email2id[email] = len(email2id)
            # 接下来需要对一个账户的所有邮箱进行连通
            first_email_id = email2id[emails[0]]
            curr_email_id = email2id[email]
            uf.union(first_email_id,curr_email_id)
    # 该连通的已经连通了

    ans = collections.defaultdict(list)
    for email,idx in email2id.items():
        parent_idx = uf.find(idx)
        ans[parent_idx].append(email)
    # print(ans)
    res = []

    id2email = {}
    for (k,v) in email2id.items():
        id2email[v] = k

    for idx,l in ans.items():
        acc = []
        name = email2name[id2email[idx]]
        acc.append(name)
        l.sort()
        acc.extend(l)
        res.append(acc.copy())
    return res

accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
res = accountsMerge(accounts)
print(res)
