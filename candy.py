class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        size = len(ratings)
        x = [1 for i in range(size)]
        inc = 2
        for i in range(1, size):
            if ratings[i] > ratings[i - 1]:
                x[i] = max(x[i], inc)
                inc += 1
            else:
                inc = 2
        inc = 2
        for i in range(size - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                x[i] = max(x[i], inc)
                inc += 1
            else:
                inc = 2
        return sum(x)


if __name__ == '__main__':
    # x = [2, 1, 3, 5, 6, 2]
    x = [4, 2, 3, 4, 1]
    solution = Solution()
    print solution.candy(x)
