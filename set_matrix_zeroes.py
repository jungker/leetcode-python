class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        row = [False for i in range(n)]
        col = [False for i in range(m)]
        for i in range(m):
            for j in range(n):
                if not matrix[i][j]:
                    row[j] = col[i] = True
        for i in range(m):
            if col[i]:
                matrix[i] = [0 for j in range(n)]
        for j in range(n):
            if row[j]:
                for i in range(m):
                    matrix[i][j] = 0


if __name__ == '__main__':
    m = [
        [1, 2, 0],
        [0, 1, 3],
        [4, 3, 0]
    ]
    solution = Solution()
    solution.setZeroes(m)
    print m
