class Solution(object):
    def remove_duplicates(self, nums):
        size = len(nums)
        if size < 2:
            return size
        j = 0
        for i in range(1, size):
            if nums[i] != nums[j]:
                nums[j + 1] = nums[i]
                j += 1
        return j + 1


if __name__ == '__main__':
    x = [1, 1, 2, 2, 3]
    solution = Solution()
    length = solution.remove_duplicates(x)
    print x[:length]
