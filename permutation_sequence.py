class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        x = range(1, n + 1)
        k -= 1
        res = []
        f = self.factorial(n - 1)
        for i in range(n - 1, 0, -1):
            j = k / f
            res.append(x[j])
            x.pop(j)
            k %= f
            f /= i
        res.append(x[0])
        res = ''.join([str(i) for i in res])
        return res

    def factorial(self, n):
        res = 1
        for i in range(1, n + 1):
            res *= i
        return res


if __name__ == '__main__':
    solution = Solution()
    print solution.getPermutation(4, 6)
