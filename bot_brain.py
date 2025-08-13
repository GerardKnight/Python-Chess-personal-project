import moves

def promote(board):
    out=board_copy(board)
    for i in range(8):
        if out[0][i]==1:
            out[0][i]=5
        if out[7][i]==-1:
            out[7][i]=-5
    return out

def board_copy(to_copy):
    out=[]
    for i in range(len(to_copy)):
        out.append([])
        for j in range(len(to_copy[i])):
            out[i].append(to_copy[i][j])
    return out

def board_evauluate(board,team):
    values=(0,1,5,3,3,8,1000,-1000,-8,-3,-3,-5,-1)
    out=0
    for i in range(8):
        for j in range(8):
            out+=values[board[i][j]]
    return out*team

def bot_move(board,team,prev_board,king_has_moved,rooks_have_moved,depth,pruning_num=0):
    func_list=['']
    func_list.append(moves.pawn_valid_moves)
    func_list.append(moves.rook_valid_moves)
    func_list.append(moves.knight_valid_moves)
    func_list.append(moves.bishop_valid_moves)
    func_list.append(moves.queen_valid_moves)
    func_list.append(moves.king_valid_moves)
    moves_from=[]
    moves_to=[]
    for i in range(8):
        for j in range(8):
            if board[i][j]*team>0:
                moves_temp=func_list[board[i][j]*team](j,i,board,prev_board,team,False,(False,False))
                moves_to=moves_to+moves_temp
                moves_from=moves_from+[[i,j]]*len(moves_temp)
    evauluations=[0]*max(1,len(moves_to))
    if depth==0:
        for i in range(len(moves_from)):
            board_temp=board_copy(board)
            board_temp[moves_to[i][0]][moves_to[i][1]]=board_temp[moves_from[i][0]][moves_from[i][1]]
            board_temp[moves_from[i][0]][moves_from[i][1]]=0
            evauluations[i]=board_evauluate(promote(board_temp),team)
            if evauluations[i]>pruning_num:
                break
        return max(evauluations)
    elif depth==3:
        big=-10000
        for i in range(len(moves_from)):
            board_temp=board_copy(board)
            board_temp[moves_to[i][0]][moves_to[i][1]]=board_temp[moves_from[i][0]][moves_from[i][1]]
            board_temp[moves_from[i][0]][moves_from[i][1]]=0
            evauluations[i]=-bot_move(board_temp,-team,prev_board,king_has_moved,rooks_have_moved,depth-1,-big)
            if evauluations[i]>big:
                big=evauluations[i]
        best=evauluations.index(max(evauluations))
        board_temp=board_copy(board)
        board_temp[moves_to[best][0]][moves_to[best][1]]=board_temp[moves_from[best][0]][moves_from[best][1]]
        board_temp[moves_from[best][0]][moves_from[best][1]]=0
        return promote(board_temp)
    else:
        big=-10000
        for i in range(len(moves_from)):
            board_temp=board_copy(board)
            board_temp[moves_to[i][0]][moves_to[i][1]]=board_temp[moves_from[i][0]][moves_from[i][1]]
            board_temp[moves_from[i][0]][moves_from[i][1]]=0
            evauluations[i]=bot_move(board_temp,-team,prev_board,king_has_moved,rooks_have_moved,depth-1,-big)
            if evauluations[i]>big:
                big=evauluations[i]
            if evauluations[i]>pruning_num:
                break
        return max(evauluations)
