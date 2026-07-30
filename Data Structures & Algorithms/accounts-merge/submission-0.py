class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        

        class UnionFind:

            def __init__(self, size):
                self.parent = [i for i in range(size)]
                self.rank = [0] * size


            def find(self, i: int) -> int:
                if self.parent[i] != i:
                    self.parent[i] = self.find(self.parent[i])
                return self.parent[i]

            def union(self, i:int, j: int) -> bool:
                root_i = self.find(i)
                root_j = self.find(j)


                if root_i != root_j:
                    if self.rank[root_i] < self.rank[root_j]:
                        self.parent[root_i] = root_j
                    elif self.rank[root_i] > self.rank[root_j]:
                        self.parent[root_j] = root_i

                    else:
                        self.parent[root_j] = root_i
                        self.rank[root_i] += 1

                    return True
                return False

            
        uf = UnionFind((len(accounts)))
        email_to_account = {}

        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in email_to_account:
                    uf.union(i, email_to_account[email])
                else:
                    email_to_account[email] = i

        root_to_emails = defaultdict(list)

        for email, i in email_to_account.items():
            root = uf.find(i)
            root_to_emails[root].append(email)

        res = []

        for root, emails in root_to_emails.items():
            name = accounts[root][0]
            res.append([name] + sorted(emails))

        return res

        

