class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        size1 = len(haystack)
        size2 = len(needle)
        i = j = 0
        while i < size1 and j < size2:
            if haystack[i] == needle[j]:
                j += 1
            else:
                i -= j
                j = 0
            i += 1
        if j == size2:
            return i - j
        return -1


if __name__ == '__main__':
    hay = "to be or not to be, it's a question"
    need = 'r not to '
    solution = Solution()
    print solution.strStr(hay, need)
