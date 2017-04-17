class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        size = len(nums)
        res = []
        if size < 3:
            return res
        nums.sort()
        d = {}
        for i in range(size - 1):
            for j in range(i + 1, size):
                t = nums[i] + nums[j]
                if t not in d:
                    d[t] = [(i, j)]
                else:
                    d[t].append((i, j))
        for k in range(size):
            t = -nums[k]
            if t not in d:
                continue
            for (i, j) in d[t]:
                if k > j:
                    res.append((nums[i], nums[j], nums[k]))
        res = set(res)
        res = [list(i) for i in res]
        # for i in range(size - 2):
        #     if i > 0 and nums[i] == nums[i - 1]:
        #         continue
        #     j, k = i + 1, size - 1
        #     while j < k:
        #         t = nums[i] + nums[j] + nums[k]
        #         if t == 0:
        #             res.append([nums[i], nums[j], nums[k]])
        #             while j < k and nums[j] == nums[j + 1]:
        #                 j += 1
        #             while j < k and nums[k] == nums[k - 1]:
        #                 k -= 1
        #             j += 1
        #             k -= 1
        #         elif t < 0:
        #             j += 1
        #         else:
        #             k -= 1
        return res


if __name__ == '__main__':
    x = [-1, 0, 1, 2, -1, -4]
    # x = [0, 0, 0]
    solution = Solution()
    print solution.threeSum(x)
