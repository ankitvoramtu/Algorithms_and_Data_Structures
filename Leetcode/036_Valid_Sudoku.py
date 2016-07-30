class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # Check each row
        for row in range(9):
            marker = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
            for col in range(9):
                cur = board[row][col]
                if cur != '.':
                    cur = ord(cur) - ord('0')
                    if marker[cur] == 1:
                        marker[cur] = 0
                    else:
                        return False

        # Check each column
        for col in range(9):
            marker = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
            for row in range(9):
                cur = board[row][col]
                if cur != '.':
                    cur = ord(cur) - ord('0')
                    if marker[cur] == 1:
                        marker[cur] = 0
                    else:
                        return False

        # Check each square
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                marker = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
                for j in range(3):
                    for i in range(3):
                        cur = board[row + i][col + j]
                        if cur != '.':
                            cur = ord(cur) - ord('0')
                            if marker[cur] == 1:
                                marker[cur] = 0
                            else:
                                return False
        return True
# Time: O(1)
# Space: O(1)
