class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        num = 0
        for i in S :
            if i in J:
                num=num + 1
        return num
            
        



if __name__=='__main__':
    J = "aA"
    S = "aAAbbbb"
    sl =Solution()
    print(sl.numJewelsInStones(J,S))
    
