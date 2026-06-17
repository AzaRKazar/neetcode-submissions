class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # for row in range(9):
        #     seen=[]
        #     for col in range(9):
        #         value=board[row][col]
        #         if value in seen and value!=".":
        #             return False
        #         seen.append(value)
        # for col in range(9):
        #     seen=[]
        #     for row in range(9):
        #         value=board[row][col]
        #         if value in seen and value!=".":
        #             return False
        #         seen.append(value)

        # for row_box in [0,3,6]:
        #     for column_box in [0,3,6]:
        #         seen=[]
        #         for row in range(row_box,row_box+3):
        #             for col in range(column_box,column_box+3):
        #                 value=board[row][col]
        #                 if value in seen and value!=".":
        #                     return False
        #                 seen.append(value)
        # return True
        # rows={i:set() for i in range(9)}
        # cols={j:set() for j in range(9)}
        # boxes={(r,c):set() for r in range(3) for c in range(3)}
            

        # for i in range(9):
        #     for j in range(9):
        #         value=board[i][j]
        #         if value==".":
        #             continue
        #         if value in boxes[(i//3),(j//3)] or value in cols[j] or value in rows[i]:
        #             return False
                
        #         cols[j].add(value)
        #         rows[i].add(value)
        #         boxes[(i//3),(j//3)].add(value)
        # return True

        # seen=set()
        # for i in range(9):
        #     for j in range(9):
        #         value=board[i][j]
        #         if value == ".":
        #             continue
        #         if (value, "row", i) in seen or (value, "col", j) in seen or (value, "box", i//3, j//3) in seen:
        #             return False
        #         seen.add((value,"col",j))
        #         seen.add((value,"row",i))
        #         seen.add((value,"box",i//3,j//3))
        # return True


        for i in range(len(board)):
            set_row=set()
            for j in range(len(board[i])):
                if board[i][j] == ".":
                    continue
                if board[i][j] in set_row:
                    return False
                set_row.add(board[i][j])
        
        for i in range(len(board[0])):
            set_col=set()
            for j in range(len(board)):
                val=board[j][i]
                if val =='.':
                    continue
                if val in set_col:
                    return False
                
                
                































