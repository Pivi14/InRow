def start_board():
    matrix=[]
    size=1
    while size<3 or size>10:
        size=int(input("The size of the board: "))
    for i in range(size):
        row=[]
        matrix.append(row)
        for y in range(size):
            row.append(0)
    return matrix



def player_move(matrix):
    valid_coordinate=False
    max_lenght=len(matrix)
    while valid_coordinate==False:
        row=int(input("Give a row: "))-1
        col=int(input("Give a column: "))-1
        if (row<=max_lenght and row>0 and col<=max_lenght and col>0):
            if matrix[row][col]==0:
                valid_coordinate=True
        else:
            print("Wrong input, try again!")
    return row,col
    
def move(matrix,coord,player):
    if player==1:
        matrix[coord[0]][coord[1]]=1
    if player==2:
        matrix[coord[0]][coord[1]]=2
    return matrix


if __name__ == '__main__':
    board = start_board()
    coord=player_move(board)
    player=1
    move(board,coord,player)
    
        
        

        