#开始居然想用递归。。。结果过50好像就不行了。实验时想起来还有斐波那契数列。。就是数组上限不好确定，题目也没给，，于是写了10000过了


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        lst = []
        lst.append(0)
        lst.append(1)
        lst.append(2)
        for i in range(10000):
            lst.append(lst[-1]+lst[-2])

        return lst[n]
        

            



if __name__=='__main__':
    sl = Solution()
    print(sl.climbStairs(4))