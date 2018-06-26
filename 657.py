#C:\Users\thinkpad\Desktop\leetcode_solve\VENV\Scripts
class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        movex =0 
        movey = 0
        for i in moves:
            if i=='U':
                movex = movex
                movey = movey + 1
            if i=='R':
                movex = movex + 1
                movey=movey
            if i=='L':
                movex = movex - 1
                movey=movey
            if i=='D':
                movex = movex
                movey = movey - 1
        
        if movex == 0 and movey == 0:
            return True
        else :
            return False 
                
        




if __name__=='__main__':
    sl=Solution()
    moves = "LLUURDD"
    print(sl.judgeCircle(moves))