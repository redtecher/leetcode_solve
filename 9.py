class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        lst = list(x)

        print(lst)

        indexo = range((len(lst)-1)/2+1)
        flag = 1
        for i in indexo:
            print(lst[i],lst[-i])
            if lst[i]==lst[-i]:
                continue
            else :
                flag =0 
                break
        
        return flag
        
        




if __name__=='__main__':
    sl= Solution()
    if sl.isPalindrome('121') :
        print('true')
    else :
        print('false')

