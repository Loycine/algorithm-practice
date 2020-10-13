class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        for i in range(9):
            cnt = [0 for k in range(10)]
            for j in range(9):
                if(board[i][j] == "."):
                    continue
                element = (int)(board[i][j])
                cnt[element] = cnt[element] + 1
                if(cnt[element] > 1):
                    print("row")
                    return False
        
        for i in range(9):
            cnt = [0 for k in range(10)]
            for j in range(9):
                if(board[j][i] == "."):
                    continue
                element = (int)(board[j][i])
                cnt[element] = cnt[element] + 1
                if(cnt[element] > 1):
                    print("coloum")
                    return False
        
        for i in range(9):
            cnt = [0 for k in range(10)]
            str = ""
            for j in range(9):
                x = i//3 * 3 + j // 3
                y = i%3 * 3 + j%3
                str = str + f"({x},{y})"
                if(board[x][y] == "."):
                    continue
                element = (int)(board[x][y])
                cnt[element] = cnt[element] + 1
                if(cnt[element] > 1):
                    print("sub-boxes")
                    return False
            print(str)

        return True