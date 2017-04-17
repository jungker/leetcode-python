class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        size = len(nums)
        j = 0
        for i in range(size):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
        return j


if __name__ == '__main__':
    x = [3, 2, 2, 3]
    target = 3
    solution = Solution()
    print solution.removeElement(x, target)
    print x
