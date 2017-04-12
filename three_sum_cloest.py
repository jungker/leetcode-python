class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        size = len(nums)
        nums.sort()
        res = i = 0
        import sys
        minGap = sys.maxint
        while i < size:
            j = i + 1
            k = size - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                gap = abs(sum - target)
                if gap < minGap:
                    minGap = gap
                    res = sum
                if sum < target:
                    j += 1
                else:
                    k -= 1
            i += 1
        return res


if __name__ == '__main__':
    x = [-1, 2, 1, 4]
    target = 1
    solution = Solution()
    print solution.threeSumClosest(x, target)

