# 1176 - Design A Leaderboard
# Date: 2024-03-17
# Runtime: 46 ms, Memory: 17.4 MB
# Submission Id: 1206300258


from sortedcontainers import SortedDict

class Leaderboard:

    def __init__(self):
        self.sorted_board = SortedDict()
        self.board = defaultdict(int)

    def addScore(self, playerId: int, score: int) -> None:
        prev_score = self.board[playerId]
        if prev_score:
            if self.sorted_board[-prev_score] == 1:
                self.sorted_board.pop(-prev_score)
            else:
                self.sorted_board[-prev_score] -= 1

        new_score = prev_score + score
        self.board[playerId] = new_score
        self.sorted_board[-new_score] = self.sorted_board.get(-new_score, 0) + 1

    def top(self, K: int) -> int:
        res = 0
        for key, value in self.sorted_board.items():
            res -= key * min(value, K)
            K -= value
            if K <= 0:
                break
        return res

    def reset(self, playerId: int) -> None:
        prev_score = self.board[playerId]
        if prev_score:
            if self.sorted_board[-prev_score] == 1:
                self.sorted_board.pop(-prev_score)
            else:
                self.sorted_board[-prev_score] -= 1
        self.board[playerId] = 0
        


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)