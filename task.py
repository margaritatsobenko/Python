import sys
"""
В очередной онлайн игре игроки, как обычно, сражаются с монстрами и набирают опыт.
Для того, чтобы сражаться с монстрами, они объединяются в кланы. После победы над монстром, 
всем участникам клана, победившего его, добавляется одинаковое число единиц опыта. 
Особенностью этой игры является то, что кланы никогда не распадаются и из клана нельзя выйти.
 Единственная доступная операция — объединение двух кланов в один.
Поскольку игроков стало уже много, вам поручили написать систему учета текущего опыта игроков.

В следующих m строках содержатся описания запросов. Запросы бывают трех типов:

join X Y — объединить кланы, в которые входят игроки X и Y (если они уже в одном клане, то ничего не меняется).
add X V — добавить V единиц опыта всем участникам клана, в который входит игрок X (1 ≤ V ≤ 100).
get X — вывести текущий опыт игрока X.

Изначально у всех игроков 0 опыта и каждый из них состоит в клане, состоящим из него одного.
"""
class DSU:
    def __init__(self, n):
        self.n = n
        self.parent = [i for i in range(n)]
        self.score = [0 for _ in range(n)]
        self.size = [1 for _ in range(n)]

    def join(self, x, y):  # объединяет множество, в котором x, и множество с у
        x = self.find_set(x)
        y = self.find_set(y)
        if x != y:
            if self.size[x] < self.size[y]:
                x, y = y, x
            self.parent[y] = x
            self.score[y] -= self.score[x]
            self.size[x] += self.size[y]

    def find_set(self, x):  # возвращает, в каком множестве находится х
        if x == self.parent[x]:
            return x
        return self.find_set(self.parent[x])

    def add(self, x, v):
        l = self.find_set(x)
        self.score[l] += v

    def get(self, x):

        ans = 0
        while x != self.parent[x]:
            ans += self.score[x]
            x = self.parent[x]

        ans += self.score[x]
        print(ans)


if __name__ == '__main__':

    n, m = map(int, sys.stdin.readline().split())

    query = []
    for i in range(m):
        q = sys.stdin.readline().split()
        if q[0] == 'join' or q[0] == 'add':
            x = int(q[1])
            y = int(q[2])
            query += [(q[0], x, y)]
        else:
            x = int(q[1])
            query += [(q[0], x)]

    dsu = DSU(n)
    for j in query:
        if j[0] == 'join':
            dsu.join(j[1] - 1, j[2] - 1)
        elif j[0] == 'add':
            dsu.add(j[1] - 1, j[2])
        else:
            dsu.get(j[1] - 1)