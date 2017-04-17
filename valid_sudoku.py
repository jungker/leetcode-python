class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            exist = [False for k in range(9)]
            for j in range(9):
                t = board[i][j]
                if t == '.':
                    continue
                t = int(t) - 1
                if not exist[t]:
                    exist[t] = True
                else:
                    return False
            exist = [False for k in range(9)]
            for j in range(9):
                t = board[j][i]
                if t == '.':
                    continue
                t = int(t) - 1
                if not exist[t]:
                    exist[t] = True
                else:
                    return False
        for i in range(3):
            for j in range(3):
                exist = [False for k in range(9)]
                for k in range(3 * i, 3 * i + 3):
                    for l in range(3 * j, 3 * j + 3):
                        t = board[k][l]
                        if t == '.':
                            continue
                        t = int(t) - 1
                        if not exist[t]:
                            exist[t] = True
                        else:
                            return False
        return True


if __name__ == '__main__':
    board = [
        ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
        ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
        ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
        ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
        ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
        ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
        ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
        ['.', '.', '.', '4', '.', '9', '.', '.', '5'],
        ['.', '.', '.', '.', '8', '.', '.', '7', '9']
    ]
    solution = Solution()
    print solution.isValidSudoku(board)
