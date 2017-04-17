class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        size = len(nums)
        if size < 2:
            return []
        d = {}
        res = []
        for i in range(size):
            if nums[i] not in d:
                d[target - nums[i]] = i
            else:
                res = [d[nums[i]], i]
        return res


if __name__ == '__main__':
    x = [2, 7, 11, 15]
    target = 9
    solution = Solution()
    print solution.twoSum(x, target)
