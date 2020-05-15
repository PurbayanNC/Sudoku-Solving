## Input
## Here zeros are considered as empty position

board = [
    [0,0,0,0,0,0,0,0,0],
    [0,5,9,4,0,0,1,0,0],
    [7,6,4,0,0,2,0,3,0],
    [0,2,0,0,6,1,0,0,4],
    [0,0,0,0,0,0,0,0,0],
    [0,8,0,0,2,5,0,0,7],
    [5,7,6,0,0,3,0,9,0],
    [0,1,2,6,0,0,8,0,0],
    [0,0,0,0,0,0,0,0,0]
    ]


#===========================================================

## Function to print the board

def print_board(bo):
    for i in range(9):
        if i%3==0 and i!=0:
            print("-----------------------")
        for j in range(9):
            if j%3==0 and j!=0:
                print(" | ",end = "")
            if j == 8:
                print(bo[i][j])
            else:
                print(bo[i][j],"", end = "")
                
#===========================================================
                
## Function to check the empty(denoted by zero here)
                
def is_empty(bo):
    for i in range(9):
        for j in range(9):
            if bo[i][j] == 0:
                return (i,j)   # pos(row, col)
            
 
#============================================================

## Function to check the validity of a number placed in an empty position
            
def is_valid(bo,num,pos):
    
    ## Check for row
    
    for i in range(9):
        if bo[pos[0]][i] == num and i != pos[1]:
            return False
    
    
    ## Check for column
    
    for j in range(9):
        if bo[j][pos[1]] == num and j != pos[0]:
            return False
       
    
    ## Check 3X3 box position(Grid) of the empty position
    
    row = pos[0] // 3
    col = pos[1] // 3
    
    
    ## Iterate through the 3X3 box of the empty position for checking
    
    for i in range(row*3, row*3 + 3):
        for j in range(col * 3, col*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False
    
    
    return True ## If the number placed at the empty position is valid
                     
    
#===================================================================
                     
## Function to solve the Sudoku Board using Backtracking Algorithm

def to_solve(bo):
    found = is_empty(bo)
    if not found:
        return True
    else:
        row,col = found

    for i in range(1,10):
        if is_valid(bo,i,(row,col)):
            bo[row][col] = i

            if to_solve(bo): ## Recurssive function
                return True  ## If False it goes to next step , else it goes recursively
                             ## ultill the whole board is solved

            bo[row][col] = 0 ## Backtracking Algorithm is applied here


    return False ## If no number is valid at a position

#===========================================================

print("\n<<================**BEFORE SOLVING**================>>\n")
print_board(board) ## Printing the board before solving

to_solve(board)  ## Calling the function to solve the board

print("\n<<================**AFTER SOLVING**================>>\n")
print_board(board)  ## Printing the board after solving 