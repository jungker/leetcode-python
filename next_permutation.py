class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        if size < 2:
            return
        i = size - 2
        while i >= 0:
            if nums[i] < nums[i + 1]:
                break
            i -= 1
        j = size - 1
        while j >= 0:
            if nums[j] > nums[i]:
                break
            j -= 1
        if i >= 0 and j >= 0:
            nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1:] = reversed(nums[i + 1:])


if __name__ == '__main__':
    # x = [1, 2, 3, 4]
    x = [1, 2]
    solution = Solution()
    for i in range(24):
        print x
        solution.nextPermutation(x)
