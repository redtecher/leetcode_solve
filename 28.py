class Solution:
    def strStr(self, haystack, needle):
        result = haystack.find(needle)
        return result


if __name__=='__main__':
    sl = Solution()
    print(sl.strStr("hello","bba"))
        