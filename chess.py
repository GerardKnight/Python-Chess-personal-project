import time
import moves
import bot_brain

def create_board():
    nums=[]
    for i in range(8):
        nums.append([])
        for j in range(8):
            nums[i].append(0)
    return nums

def board_print(to_print):
    dab=piece_lib()
    dab2=create_board()
    for i in range(8):
        for j in range(8):
            dab2[i][j]=dab[to_print[i][j]]
    for i in dab2:
        print(i)

def piece_lib():
    out=["            ","white pawn  ","white rook  ","white knight","white bishop","white queen ","white king  "]
    out=out+["black king  ","black queen ","black bishop","black knight","black rook  ","black pawn  "]
    return out

def init_board():
    board=create_board()
    for i in range(8):
        board[1][i]=-1
        board[6][i]=1
    board[0][0]=-2
    board[0][7]=-2
    board[7][0]=2
    board[7][7]=2
    board[0][1]=-3
    board[0][6]=-3
    board[7][1]=3
    board[7][6]=3
    board[0][2]=-4
    board[0][5]=-4
    board[7][2]=4
    board[7][5]=4
    board[0][3]=-5
    board[7][3]=5
    board[0][4]=-6
    board[7][4]=6
    return board

def pos_in_string(find_in,find_this):
    if not find_this in find_in:
        print('error, not in string')
        return None
    else:
        for i in range(len(find_in)):
            if find_in[i]==find_this:
                return i

def promote(board):
    out=board_copy(board)
    for i in range(8):
        if out[0][i]==1:
            out[0][i]=5
        if out[7][i]==-1:
            out[7][i]=-5
    return out


def player_move(board,team,prev_board,king_has_moved,rooks_have_moved):
    out=[]+board
    string_list_x='abcdefgh'
    string_list_y='87654321'
    string_list=['back']
    func_list=['']
    func_list.append(moves.pawn_valid_moves)
    func_list.append(moves.rook_valid_moves)
    func_list.append(moves.knight_valid_moves)
    func_list.append(moves.bishop_valid_moves)
    func_list.append(moves.queen_valid_moves)
    func_list.append(moves.king_valid_moves)
    for i in string_list_x:
        for j in string_list_y:
            string_list.append(i+j+" ")
    state=0
    while state>=0:
        if state==0:
            selection=input("Please select a piece.\n--->")
            selection=selection+" "
            x_selection=pos_in_string(string_list_x,selection[0])
            y_selection=pos_in_string(string_list_y,selection[1])
            if not selection in string_list:
                print("Please select a valid tile.")
            elif not board[y_selection][x_selection]*team>0:
                print("You don't have a piece there.")
            else:
                state=1
        elif state==1:
            valid_moves=func_list[abs(board[y_selection][x_selection])](x_selection,y_selection,board,prev_board,team,king_has_moved,rooks_have_moved)
            print(valid_moves)
            move_to=input("Plese select where you would like to move your piece.\n--->")
            move_to=move_to+" "
            x_move=pos_in_string(string_list_x,move_to[0])
            y_move=pos_in_string(string_list_y,move_to[1])
            move_to_coords=[y_move,x_move]
            if move_to=="back":
                state=0
            elif not move_to in string_list:
                print("Please select a valid tile.")
            elif not (y_move,x_move) in valid_moves:
                print("That piece cannot move there.")
            else:
                out=board_copy(board)
                out[y_move][x_move]=out[y_selection][x_selection]
                out[y_selection][x_selection]=0
                if abs(out[y_move][x_move])==1:
                    if x_move!=x_selection:
                        out[y_move+team][x_move]=0
                elif abs(out[y_move][x_move])==6:
                    if abs(x_selection-x_move)>1:
                        if x_move==6:
                            out[y_move][7]=0
                            out[y_move][5]=2*team
                        elif x_move==2:
                            out=[y_move][0]=0
                            out[y_move][3]=2*team
                state=-1
    return promote(out)

def print_where_can_move(locations):
    board=create_board()
    for i in locations:
        board[i[0]][i[1]]=1
    board_print(board)

def which_team(num):
    out=0
    if num>0:
        out=1
    elif num<0:
        out=-1
    return out

def art_lib():
    empty=["               ","               ","               ","               ","               ","               "]
    pawn=["               ","               ","               ","      ()       ","      )(       ","     /__\\      "]
    rook=["               ","               ","    |  |  |    ","     \\   /     ","     /   \\     ","    /_____\\    "]
    bishop=["               ","       ,       ","      (^)      ","      / \\      ","      { }      ","     {___}     "]
    knight=["   (\\_         ","   =| .\\       ","   =| (_\\      ","   =) ( \\)     ","   (   )       ","   [_____]     "]
    queen=["      _._      ","      ( )      ","      / \\      ","      | |      ","      { }      ","     {___}     "]
    king=["       +       ","      ( )      ","      / \\      ","      | |      ","      { }      ","     {___}     "]
    out=(empty,pawn,rook,knight,bishop,queen,king)
    return out

def board_print_art(board):
    pieces=['empty','pawn','rook','knight','bishop','queen','king']
    piece_art=art_lib()
    colours=('','red','black')
    letters='abcdefgh'
    numbers='87654321'
    top_row="  "
    for i in range(8):
        top_row=top_row+letters[i]*15+" "
    print(top_row)
    print('_'*129)
    for i in range(8):
        for j in range(6):
            print(numbers[i]+'|',end='')
            for k in range(8):
                to_print=piece_art[abs(board[i][k])][j]
                if board[i][k]<0:
                    to_print=to_print.replace("   ","...")
                print(to_print,end='')
                print('|',end='')
            print()
        print('_'*129)
    print(top_row)

def board_copy(to_copy):
    out=[]
    for i in range(len(to_copy)):
        out.append([])
        for j in range(len(to_copy[i])):
            out[i].append(to_copy[i][j])
    return out

def check_piece_moved(x,y,piece_num,board):
    good=True
    if board[y][x]!=piece_num:
        good=False
    return good

def check_has_king(board):
    good=[False]*3
    for i in range(8):
        for j in range(8):
            if board[i][j] in (6,-6):
                good[board[i][j]//6]=True
    return good

def player_select():
    print("Would you like to play singleplayer, or multiplayer?")
    select_sp=True
    while select_sp:
        sp=input("s/m --->")
        if sp=="s":
            print("Would you like to go first or second?")
            select_num=True
            while select_num:
                num=input("1/2 --->")
                if num=="1":
                    return -1
                elif num=="2":
                    return 1
                elif num=="back":
                    select_num=False
                    print("Would you like to play singleplayer, or multiplayer?")
                else:
                    print("Please enter a valid input.")
        elif sp=="m":
            return 0
        else:
            print("Please enter a valid input.")
                

def main():
    times=[time.perf_counter()]
    playing=True
    team=1
    teams=['','1','2']
    board=init_board()
    prev_boards=[init_board(),init_board()]
    turn=0
    have_moved=[True]*7
    checking_x=('',4,7,0,0,7,4)
    checking_y=('',7,7,7,0,0,0)
    checking_piece=('',6,2,2,-2,-2,-6)
    players=player_select()
    while playing:
        for i in range(1,7):
            j=i*team
            if have_moved[j]:
                have_moved[j]=check_piece_moved(checking_x[j],checking_y[j],checking_piece[j],board)
        board_print_art(board)
        print("It's your turn, player "+teams[team]+'.')
        rooks_have_moved_2=[have_moved[3*team],have_moved[2*team]]
        if team==players:
            board=bot_brain.bot_move(board,team,prev_boards[turn],have_moved[team],rooks_have_moved_2,3)
        else:
            board=player_move(board,team,prev_boards[turn],have_moved[team],rooks_have_moved_2)
        times.append(time.perf_counter())
        #print(times[-1]-times[-2])
        prev_boards.append(board_copy(board))
        team*=-1
        turn+=1
        has_won=check_has_king(board)
        if not has_won[2]:
            playing=False
            print("Player 1 has won!")
        elif not has_won[1]:
            playing=False
            print("Player 2 has won!")
    input()

main()
