class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        if not matrix:
            return res
        res.extend(matrix[0])
        matrix.pop(0)
        if matrix:
            res.extend(self.spiralOrder(zip(*matrix)[::-1]))
        return res


if __name__ == '__main__':
    m = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    solution = Solution()
    print solution.spiralOrder(m)
