class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [[set() for _ in range(3)] for _ in range(3)]
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == ".":
                    continue
                rowSet = rows[r]
                colSet = cols[c]
                boxSet = boxes[r // 3][c // 3]
                if board[r][c] in rowSet or board[r][c] in colSet or board[r][c] in boxSet:
                    return False
                rowSet.add(board[r][c])
                colSet.add(board[r][c])
                boxSet.add(board[r][c])
        return True
