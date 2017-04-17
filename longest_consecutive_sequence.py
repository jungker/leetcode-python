class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for i in nums:
            if i not in d:
                d[i] = False
        res = 0
        for i in nums:
            if d[i]:
                continue
            j = i
            t = 0
            while j in d:
                t += 1
                d[j] = True
                j -= 1
            j = i + 1
            while j in d:
                t += 1
                d[j] = True
                j += 1
            res = max(res, t)
        return res


if __name__ == '__main__':
    x = [100, 4, 200, 1, 3, 2]
    solution = Solution()
    print solution.longestConsecutive(x)
