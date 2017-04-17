class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = [0]
        for i in range(n):
            t = 1 << i
            for j in range(len(res) - 1, -1, -1):
                res.append(t | res[j])
        return res


if __name__ == '__main__':
    solution = Solution()
    print solution.grayCode(3)
