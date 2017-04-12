class Solution(object):
    def remove_duplicates(self, nums):
        size = len(nums)
        if size < 3:
            return size
        j = 0
        for i in range(2, size):
            if nums[j] != nums[i]:
                nums[j + 2] = nums[i]
                j += 1
        return j + 2


if __name__ == '__main__':
    x = [1, 1, 1, 2, 2, 2, 3, 3]
    solution = Solution()
    length = solution.remove_duplicates(x)
    print x[:length]
