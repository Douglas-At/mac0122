import random
from collections import Counter

def print_sudoku(board):
    for i in range(9):
        for j in range(9):
            print(board[i][j], end=" ")
        print()

def save_sudoku_to_file(board, filename):
    with open(filename, "w") as file:
        for row in board:
            file.write(" ".join(str(num) for num in row))
            file.write("\n")

def generate_sudoku():
    # Initialize an empty 9x9 Sudoku grid
    board = [[random.randint(1, 8) for _ in range(9)] for _ in range(9)]

    # Fill the diagonal subgrids

    return board

def remove_numbers(board, num_to_remove):
    # Randomly remove numbers while keeping the solution unique
    for _ in range(num_to_remove):
        i, j = random.randint(0, 8), random.randint(0, 8)
        while board[i][j] == 0:
            i, j = random.randint(0, 8), random.randint(0, 8)
        board[i][j] = 0

    return board

def verificar(board):
    
    # todas as colunas 
    # todos os cubos 

    #linhas
    def duplicado(lista):
        seen = set()
        for num in lista:
            if num != 0:
                if num in seen:
                    return True
                seen.add(num)

        return False
    
    for row in board:
        if duplicado(row):
            return False,1

    for i in range(0,9):
        
        col = [board[j][i] for j in range(0,9)]
        
        if duplicado(col):
            return False,2
        
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            subgrid = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
            if duplicado(subgrid):
                return False,3
    return True,"liso"
    


for i in range(0,100):
    sudoku = generate_sudoku()
    sudoko_final = remove_numbers(sudoku,64)
    
    a,b = verificar(sudoko_final)
    if a == True:
        print(a,b)
        print_sudoku(sudoko_final)
    
    

quit()
if __name__ == "__main__":
    # Generate a Sudoku grid
    sudoku_grid = generate_sudoku()
    sudoko_final = remove_numbers(sudoku_grid, 64)
    verificar(sudoko_final)
    
    #save_sudoku_to_file(sudoku_with_17_filled, "sudoku.txt")
