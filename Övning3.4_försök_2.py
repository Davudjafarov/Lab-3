# Dictionary = {key: value}
# Tuple = (,)
# list = []
# String ()




#Funktion som skapar tom dictionary
def new_board():
    return {}

def is_free(board, col, row):
    if (col, row) not in board:
        return "Spot is empty (True)"
    else:
        return "Spot is taken (False)"


def place_piece(board, col, row, piece):
    if is_free(board, col, row) == "Spot is empty (True)":
        board[(col, row)] = piece
        return f"{piece} has been placed on ({col},{row})"
    else:
        return "Spot is taken"


    #Om input col, row finns som key i board, returnera false, platsen är tagen
def get_piece(board, col, row):
    if (col, row) in board:
        return board[(col, row)] # Returnera pjäsen(value) för den platsen
    else:
        return "Empty (False)"


def remove(board, col, row):
    piece = get_piece(board, col, row)
    if piece != "Empty (False)":
        board.pop((col, row))
    else: 
        return "Empty Spot, cant delete (False)"

def move(board, from_col, from_row, to_col, to_row):
    piece = get_piece(board, from_col, from_row)
    if piece == "Empty (False)" or is_free(board, to_col, to_row) == "Spot is taken (False)":
        #Om spelpjäsen inte finns eller om platsen är taget return False
        return "Går inte att flytta (False)"
    else:
        board[(to_col, to_row)] = piece #Spelpjäsen får en ny plats
        board.pop((from_col, from_row)) #Ta bort gamla kordinaterna för piece



# for key, value in board.items():
# Key i vårat fall är (col, row)

def count(board, axis, index_value, piece):
    count = 0
    if axis == "col":
        for (col, row), value in board.items(): #gå igenom alla pjäser
            if col == index_value and value == piece: #Och för att sedan kolla om col == index och om spelpjäsen finns i board
                count += 1
    elif axis == "row":
        for (col, row), value in board():
            if row == index_value and value == piece:
                count += 1
    else:
        print("Incorrect input")
    return count

#_______________________ Input _____________________________________________
board = new_board()
print(is_free(board, 500, 100))
print(place_piece(board, 500, 100, "spelare1"))