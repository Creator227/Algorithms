from collections import namedtuple


class Tree:
    def __init__(self, a):
        self.a = a
        self.t = [100000] * len(a)*4
        self.build_tree(1, 0, len(self.a)-1)

    def build_tree(self, v, tl, tr):
        if tl == tr:
            self.t[v] = self.a[tl]
        else:
            mid = (tl + tr) // 2
            self.build_tree(v * 2, tl, mid)
            self.build_tree(v * 2 + 1, mid + 1, tr)
            self.t[v] = min(self.t[v * 2], self.t[v * 2 + 1])

    def slice(self, v, tl, tr, l, r):
        if l > r:
            return 100000
        if tl == l and tr == r:
            return self.t[v]
        mid = (tl + tr) // 2
        return min(self.slice(v*2, tl, mid, l, min(r, mid)), self.slice(v*2+1, mid + 1, tr, max(l, mid + 1), r))

    def modify(self, v, tl, tr, index, new_value):
        if tl == tr:
            self.t[v] = new_value
        else:
            mid = (tl + tr) // 2
            if index <= mid:
                self.modify(v*2, tl, mid, index, new_value)
            else:
                self.modify(v * 2 + 1, mid + 1, tr, index, new_value)
            self.t[v] = min(self.t[v*2], self.t[v*2 + 1])


# each team contains 3 players - x, y, z - participant result in personal competitions
team = namedtuple('team', 'x y z')
teams = list()
with open('input.txt', 'r') as fin:
    teams_number = int(fin.readline())
    for line in fin.readlines():
        curr_team = team(*map(int, line.split()))
        teams.append(curr_team)
print(teams)
# sort all teams by first participant
teams.sort(key=lambda x: x[0])
min_intervals = Tree([100000] * teams_number * 3)

answer = teams_number

for team in teams:
    min_intervals.modify(1, 0, teams_number*3 - 1, team.y - 1, team.z)
    print(min_intervals.slice(1, 0, teams_number*3 - 1, 0, team.y - 1))
    if min_intervals.slice(1, 0, teams_number*3 - 1, 0, team.y - 1) < team.z:
        answer -= 1

with open('output.txt', 'w') as fout:
    fout.write(str(answer))
