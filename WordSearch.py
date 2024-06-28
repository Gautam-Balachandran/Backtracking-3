# Time Complexity : O(m*n*4^l), where mxn is the size of the board and l is the length of the word
# Space Complexity : O(l), due to recursion stack
class Solution:
    def __init__(self):
        self.m = 0
        self.n = 0
        self.dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def exist(self, board: list[list[str]], word: str) -> bool:
        if not board or not board[0] or not word:
            return False
        
        self.m = len(board)
        self.n = len(board[0])
        
        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] == word[0] and self.backtrack(board, word, 0, i, j):
                    return True
        return False

    def backtrack(self, board: list[list[str]], word: str, index: int, row: int, col: int) -> bool:
        # base case
        if index == len(word):
            return True
        if row < 0 or row >= self.m or col < 0 or col >= self.n or board[row][col] != word[index]:
            return False
        
        # mark the cell as visited
        temp = board[row][col]
        board[row][col] = '#'

        # explore all possible directions
        for dir in self.dirs:
            nr = row + dir[0]
            nc = col + dir[1]
            if self.backtrack(board, word, index + 1, nr, nc):
                return True

        # unmark the cell
        board[row][col] = temp
        
        return False

# Example usage:
sol = Solution()

# Example 1
board1 = [
    ['A','B','C','E'],
    ['S','F','C','S'],
    ['A','D','E','E']
]
word1 = "ABCCED"
print("Input: ABCCED")
print("Output:", sol.exist(board1, word1)) # True

# Example 2
board2 = [
    ['A','B','C','E'],
    ['S','F','C','S'],
    ['A','D','E','E']
]
word2 = "SEE"
print("\nInput: SEE")
print("Output:", sol.exist(board2, word2)) # True

# Example 3
board3 = [
    ['A','B','C','E'],
    ['S','F','C','S'],
    ['A','D','E','E']
]
word3 = "ABCB"
print("\nInput: ABCB")
print("Output:", sol.exist(board3, word3)) # False