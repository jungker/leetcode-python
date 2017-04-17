class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        size = len(nums)
        res = []
        d = {}
        nums.sort()
        for i in range(size - 1):
            for j in range(i + 1, size):
                t = nums[i] + nums[j]
                if t not in d:
                    d[t] = [(i, j)]
                else:
                    d[t].append((i, j))
        # for k in range(size - 1):
        #     for l in range(k + 1, size):
        #         t = target - nums[k] - nums[l]
        #         if t not in d:
        #             continue
        #         for (i, j) in d[t]:
        #             if k > j:
        #                 res.append((nums[i], nums[j], nums[k], nums[l]))
        for p in d:
            q = target - p
            if q not in d:
                continue
            for (i, j) in d[p]:
                for (k, l) in d[q]:
                    if i != k and i != l and j != k and j != l:
                        t = [nums[i], nums[j], nums[k], nums[l]]
                        t.sort()
                        res.append(tuple(t))
        res = [list(i) for i in set(res)]
        return res


if __name__ == '__main__':
    # x = [1, 0, -1, 0, -2, 2]
    x = [-5, 5, 4, -3, 0, 0, 4, -2]
    target = 4
    solution = Solution()
    print solution.fourSum(x, target)
