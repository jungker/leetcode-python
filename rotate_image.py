class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        size = len(matrix)
        for i in range(size / 2):
            matrix[i], matrix[size - i - 1] = matrix[size - i - 1], matrix[i]
        for i in range(size):
            for j in range(i, size):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


if __name__ == '__main__':
    m = [
        [1, 2],
        [3, 4]
    ]

    solution = Solution()
    for i in m:
        for j in i:
            print j,
        print
    print
    solution.rotate(m)
    for i in m:
        for j in i:
            print j,
        print
