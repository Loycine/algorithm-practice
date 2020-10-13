class Solution:
    # class variable
    vis = [[]]
    nodes = []
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    def dfs(self, x, y, n, m, board):
        self.vis[x][y] = True
        self.nodes.append((x,y))

        ok = False        
        for i in range(4):
            next_x = x + self.dx[i]
            next_y = y + self.dy[i]
            if(next_x >=0 and next_x < n and next_y >=0 and next_y < m):
                if(not self.vis[next_x][next_y] and board[x][y] == 'O'):
                    if(self.dfs(next_x, next_y, n, m, board)):
                        ok = True
            else:
                ok = True
        return ok


    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        if n == 0:
            return
        m = len(board[0])

        self.vis = [[False for i in range(m)] for j in range(n)]
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'X':
                    continue
                else:
                    if(not self.dfs(i, j, n, m, board)):
                        for node in self.nodes:
                            board[node[0]][node[1]] = 'X'
                    self.nodes = []