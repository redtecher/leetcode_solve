class Solution:
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n % 4 == 0:
            return False
        return True
        



if __name__=='__main__':
    sl = Solution()
    sl.canWinNim(100)
