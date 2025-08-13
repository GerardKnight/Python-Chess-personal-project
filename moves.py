def rook_valid_moves(x,y,board,prev_board,team,king_has_moved,rooks_have_moved):
    in_range=range(8)
    out=[]
    abu=True
    moves=1
    while abu:
        check=x+moves
        if not check in in_range:
            abu=False
        else:
            if board[y][check]*team>0:
                abu=False
            elif board[y][check]!=0:
                out.append((y,check))
                abu=False
            else:
                out.append((y,check))
                moves+=1
    abu=True
    moves=1
    while abu:
        check=x-moves
        if not check in in_range:
            abu=False
        else:
            if board[y][check]*team>0:
                abu=False
            elif board[y][check]!=0:
                out.append((y,check))
                abu=False
            else:
                out.append((y,check))
                moves+=1
    abu=True
    moves=1
    while abu:
        check=y+moves
        if not check in in_range:
            abu=False
        else:
            if board[check][x]*team>0:
                abu=False
            elif board[check][x]!=0:
                out.append((check,x))
                abu=False
            else:
                out.append((check,x))
                moves+=1
    abu=True
    moves=1
    while abu:
        check=y-moves
        if not check in in_range:
            abu=False
        else:
            if board[check][x]*team>0:
                abu=False
            elif board[check][x]!=0:
                out.append((check,x))
                abu=False
            else:
                out.append((check,x))
                moves+=1
    return out

def bishop_valid_moves(x,y,board,prev_board,team,king_has_moved,rooks_have_moved):
    in_range=range(8)
    out=[]
    moves=1
    abu=True
    while abu:
        check_x=x+moves
        check_y=y+moves
        if not ((check_x in in_range) and (check_y in in_range)):
            abu=False
        else:
            if board[check_y][check_x]*team>0:
                abu=False
            elif board[check_y][check_x]!=0:
                out.append((check_y,check_x))
                abu=False
            else:
                out.append((check_y,check_x))
                moves+=1
    moves=1
    abu=True
    while abu:
        check_x=x-moves
        check_y=y+moves
        if not (check_x in in_range and check_y in in_range):
            abu=False
        else:
            if board[check_y][check_x]*team>0:
                abu=False
            elif board[check_y][check_x]!=0:
                out.append((check_y,check_x))
                abu=False
            else:
                out.append((check_y,check_x))
                moves+=1
    moves=1
    abu=True
    while abu:
        check_x=x+moves
        check_y=y-moves
        if not (check_x in in_range and check_y in in_range):
            abu=False
        else:
            if board[check_y][check_x]*team>0:
                abu=False
            elif board[check_y][check_x]!=0:
                out.append((check_y,check_x))
                abu=False
            else:
                out.append((check_y,check_x))
                moves+=1
    moves=1
    abu=True
    while abu:
        check_x=x-moves
        check_y=y-moves
        if not (check_x in in_range and check_y in in_range):
            abu=False
        else:
            if board[check_y][check_x]*team>0:
                abu=False
            elif board[check_y][check_x]!=0:
                out.append((check_y,check_x))
                abu=False
            else:
                out.append((check_y,check_x))
                moves+=1
    return out

def knight_valid_moves(x,y,board,prev_board,team,king_has_moved,rooks_have_moved):
    out=[]
    to_check_list=((x+2,y+1),(x+2,y-1),(x-2,y+1),(x-2,y-1),(x+1,y+2),(x+1,y-2),(x-1,y+2),(x-1,y-2))
    in_range=range(8)
    for i in range(8):
        check=to_check_list[i]
        if (check[0] in in_range and check[1] in in_range):
            if (board[check[1]][check[0]]*team<0) or (board[check[1]][check[0]]==0):
                check2=(check[1],check[0])
                out.append(check2)
    return out

def queen_valid_moves(x,y,board,prev_board,team,king_has_moved,rooks_have_moved):
    out=[]
    out=out+rook_valid_moves(x,y,board,prev_board,team,king_has_moved,rooks_have_moved)
    out=out+bishop_valid_moves(x,y,board,prev_board,team,king_has_moved,rooks_have_moved)
    return out

def king_valid_moves(x,y,board,prev_board,team,king_has_moved,rooks_have_moved):
    out=[]
    to_check_list=((x,y+1),(x,y-1),(x+1,y),(x-1,y),(x+1,y+1),(x+1,y-1),(x-1,y+1),(x-1,y-1))
    in_range=range(8)
    for i in range(8):
        check=to_check_list[i]
        if (check[0] in in_range and check[1] in in_range):
            if (board[check[1]][check[0]]*team<0) or (board[check[1]][check[0]]==0):
                check2=(check[1],check[0])
                out.append(check2)
    if team==1:
        if king_has_moved:
            if rooks_have_moved[0]:
                if board[7][1]==0 and board[7][2]==0 and board[7][3]==0:
                    out.append((7,2))
            if rooks_have_moved[1]:
                if board[7][6]==0 and board[7][5]==0:
                    out.append((7,6))
    else:
        if king_has_moved:
            if rooks_have_moved[0]:
                if board[0][1]==0 and board[0][1]==0 and board[0][1]==0:
                    out.append((0,2))
            if rooks_have_moved[1]:
                if board[0][6]==0 and board[0][5]==0:
                    out.append((0,6))
    return out

def pawn_valid_moves(x,y,board,prev_board,team,king_has_moved,rooks_have_moved):
    in_range=range(8)
    out=[]
    if team==1:
        if y-1 in in_range:
            if board[y-1][x]==0:
                out.append((y-1,x))
                if y==6:
                    if board[y-2][x]==0:
                        out.append((y-2,x))
        if y-1 in in_range and x+1 in in_range:
            if board[y-1][x+1]*team<0:
                out.append((y-1,x+1))
            elif (board[y][x+1]==-1):
                if(prev_board[y-2][x+1]==-1) and board[y-2][x+1]==0:
                    out.append((y-1,x+1))
        if y-1 in in_range and x-1 in in_range:
            if board[y-1][x-1]*team<0:
                out.append((y-1,x-1))
            elif (board[y][x-1]==-1):
                if (prev_board[y-2][x-1]==-1) and board[y-2][x-1]==0:
                    out.append((y-1,x-1))
    else:
        if y+1 in in_range:
            if board[y+1][x]==0:
                out.append((y+1,x))
                if y==1:
                    if board[y+2][x]==0:
                        out.append((y+2,x))
        if y+1 in in_range and x+1 in in_range:
            if board[y+1][x+1]*team<0:
                out.append((y+1,x+1))
            elif (board[y][x+1]==-1):
                if(prev_board[y+2][x+1]==-1) and board[y+2][x+1]==0:
                    out.append((y+1,x+1))
        if y+1 in in_range and x-1 in in_range:
            if board[y+1][x-1]*team<0:
                out.append((y+1,x-1))
            elif (board[y][x-1]==-1):
                if (prev_board[y+2][x-1]==-1) and board[y+2][x-1]==0:
                    out.append((y+1,x-1))
    return out
