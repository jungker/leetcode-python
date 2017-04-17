class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        size = len(gas)
        res = t = 0
        j = 0
        for i in range(size):
            t += (gas[i] - cost[i])
            res += (gas[i] - cost[i])
            if t < 0:
                t = 0
                j = i + 1
        return j if res > 0 else -1


if __name__ == '__main__':
    x = [2, 3, 2, 1, 5]
    y = [1, 5, 3, 1, 2]
    solution = Solution()
    print solution.canCompleteCircuit(x, y)
