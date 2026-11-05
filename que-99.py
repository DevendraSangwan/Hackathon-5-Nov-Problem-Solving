# Que-99
# board=[
#     ["5","3",".",".","7",".",".",".","."],
#     ["6",".",".","1","9","5",".",".","."],
#     [".","9","8",".",".",".",".","6","."],
#     ["8",".",".",".","6",".",".",".","3"],
#     ["4",".",".","8",".","3",".",".","1"],
#     ["7",".",".",".","2",".",".",".","6"],
#     [".","6",".",".",".",".","2","8","."],
#     [".",".",".","4","1","9",".",".","5"],
#     [".",".",".",".","8",".",".","7","9"]]
# for i in range(9):
#     r=[]
#     c=[]
#     for j in range(9):
#         if board[i][j]!=".":
#             if board[i][j]in r:
#                 print(False)
#                 break
#             r.append(board[i][j])
#         if board[j][i]!=".":
#             if board[j][i] in c:
#                 print(False)
#                 break
#             c.append(board[j][i])
#     else:
#         continue
#     break
# else:
#     for i in range(0,9,3):
#         for j in range(0,9,3):
#             box=[]
#             for r in range(i,i+3):
#                 for c in range(j,j+3):
#                     if board[r][c]!=".":
#                         if board[r][c] in box:
#                             print(False)
#                             exit()
#                         box.append(board[r][c])
#     print(True)
