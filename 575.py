class Solution:
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        myset=set()
        for i in range(candies):
            if i not in myset:
                myset.add(i)
                if len(myset) is len(candies)//2:
                    break
        
        return min(len(myset),len(candies)//2)
                    

        


if __name__=='__main__':
    sl=Solution()
    candies = [1,1,2,2,3,3]
    sl.distributeCandies(candies)
