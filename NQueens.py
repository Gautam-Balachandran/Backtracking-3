# Time Complexity : O(n!)
# Space Complexity : O(n^2)
class Solution:
    def __init__(self):
        self.result = []
        self.board = []

    def solveNQueens(self, n: int) -> list:
        if n == 0:
            return []
        self.result = []
        self.board = [[False] * n for _ in range(n)]
        self.backtrack(0)
        return self.result

    def backtrack(self, row: int):
        if row == len(self.board):
            answer = []
            for i in range(len(self.board)):
                sb = []
                for j in range(len(self.board)):
                    if self.board[i][j]:
                        sb.append('Q')
                    else:
                        sb.append('.')
                answer.append(''.join(sb))
            self.result.append(answer)
            return
        for i in range(len(self.board)):
            if self.isSafe(row, i):
                self.board[row][i] = True
                self.backtrack(row + 1)
                self.board[row][i] = False

    def isSafe(self, row: int, col: int) -> bool:
        # Check the column
        for i in range(row):
            if self.board[i][col]:
                return False
        # Check the upper left diagonal
        i, j = row, col
        while i >= 0 and j >= 0:
            if self.board[i][j]:
                return False
            i -= 1
            j -= 1
        # Check the upper right diagonal
        i, j = row, col
        while i >= 0 and j < len(self.board):
            if self.board[i][j]:
                return False
            i -= 1
            j += 1
        return True

# Example usage:
sol = Solution()

# Example 1
n1 = 4
print(sol.solveNQueens(n1))

# Example 2
n2 = 1
print(sol.solveNQueens(n2))

# Example 3
n3 = 8
print(sol.solveNQueens(n3))