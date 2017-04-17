class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        prev = cur = 1
        for i in range(n - 1):
            t = prev + cur
            prev = cur
            cur = t
        return cur


if __name__ == '__main__':
    solution = Solution()
    print solution.climbStairs(2)
