class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        rows=len(board)
        cols=len(board[0])
        neigh=[(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
        def changeing(row,col):
            live=0
            for i,j in neigh:
                new_r=row+i
                new_c=col+j
                if (new_r>=0 and new_r<rows) and (new_c>=0 and new_c<cols) and abs(board[new_r][new_c])==1:
                    live+=1
            return live
        for i in range(rows):
            for j in range(cols):
                lives=changeing(i,j)
                if board[i][j]==1:
                    if lives<2 or lives>3:
                        board[i][j]=-1
                else:
                    if lives==3:
                        board[i][j]=2
        for i in range(rows):
            for j in range(cols):
                if board[i][j]>0:
                    board[i][j]=1
                else:
                    board[i][j]=0
        
