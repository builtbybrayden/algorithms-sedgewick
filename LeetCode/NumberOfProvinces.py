class Solution:
    id = []
    sz = []
    count

    def WeightedQuickUnionUF(self, n: int):
        self.count = n
        self.id = list(range(n))
        self.sz = [1] * n

    def count(self) -> int:
        return self.count

    def connected(self, p: int, q: int) -> bool:
        return self.find(p) == self.find(q)

    def find(self, p: int) -> int:
        while(p != self.id[p]):
            p = self.id[p]
        return p

    def union(self, p: int, q: int):
        i = self.find(p)
        j = self.find(q)
        if (i is j): 
            return

        if (self.sz[i] < self.sz[j]):
            self.id[i] = j
            self.sz[j] += self.sz[i]
        else:
            self.id[j] = i
            self.sz[i] += self.sz[j]
        self.count -= 1

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        self.WeightedQuickUnionUF(len(isConnected))

        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if isConnected[i][j] == 1:
                    self.union(i, j)
        
        return self.count
    