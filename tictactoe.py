import tkinter as tk
from tkinter import messagebox
import os
global canvas_width, canvas_height
global b1, b2, b3, b4, b5, b6, b7, b8, b9
game = [-1, -1, -1, -1, -1, -1, -1, -1, -1]
player = 0
click_count = 0


def draw_board(canvas, s_width, s_height):

    canvas.create_line(s_width / 3, 0,
                       s_width / 3, s_height,
                       fill="yellow", width=2, tags="x1_line")
    canvas.create_line(2* (s_width / 3), 0, 2 * (s_width / 3), s_height,
                       fill="yellow", width=2, tags="x2_line")

    canvas.create_line(0, s_height / 3,
                       s_width, s_height / 3,
                       fill="yellow", width=2, tags="y1_line")
    canvas.create_line(0, 2 * (s_height / 3), s_width , 2* (s_height / 3),
                       fill="yellow", width=2, tags="y2_line")


def configure_game():

    
    b1 = tk.Button(canvas, bg = "light sky blue", relief="flat", activebackground= "light sky blue", command=lambda: button_click(b1, 0, 0))
    b2 = tk.Button(canvas, bg = "light sky blue", relief="flat", activebackground= "light sky blue", command=lambda: button_click(b2, 0, 1))
    b3 = tk.Button(canvas, bg = "light sky blue", relief="flat", activebackground= "light sky blue", command=lambda: button_click(b3, 0, 2))
    b4 = tk.Button(canvas, bg = "light sky blue", relief="flat", activebackground= "light sky blue", command=lambda: button_click(b4, 1, 0))
    b5 = tk.Button(canvas, bg = "light sky blue", relief="flat", activebackground= "light sky blue", command=lambda: button_click(b5, 1, 1))
    b6 = tk.Button(canvas, bg = "light sky blue", relief="flat", activebackground= "light sky blue", command=lambda: button_click(b6, 1, 2))
    b7 = tk.Button(canvas, bg = "light sky blue", relief="flat", activebackground= "light sky blue", command=lambda: button_click(b7, 2, 0))
    b8 = tk.Button(canvas, bg = "light sky blue", relief="flat", activebackground= "light sky blue", command=lambda: button_click(b8, 2, 1))
    b9 = tk.Button(canvas, bg = "light sky blue", relief="flat", activebackground= "light sky blue", command=lambda: button_click(b9, 2, 2))

    b1.place(x = 0, y = 0, width = (canvas_width / 3) - 1, height = (canvas_height / 3) - 1)
    b2.place(x = (canvas_width / 3) + 1, y = 0, width = (canvas_width / 3) - 2, height = (canvas_height / 3) - 2)
    b3.place(x = (2 * (canvas_width / 3) + 1), y=0, width = (canvas_width / 3), height = ((canvas_height / 3) - 2))

    b4.place(x = 0, y = (canvas_height / 3) + 1, width = (canvas_width / 3) - 1, height = (canvas_height / 3) - 3)
    b5.place(x = (canvas_width / 3) + 1, y = (canvas_height / 3) + 1, width = (canvas_width / 3) - 2, height = (canvas_height / 3) - 3)
    b6.place(x = (2 * (canvas_width / 3) + 1), y = (canvas_height / 3) + 1 , width = (canvas_width / 3), height = ((canvas_height / 3) - 3))

    b7.place(x = 0, y = (2 * (canvas_height / 3)) + 1, width = (canvas_width / 3) - 1, height = (canvas_height / 3) - 1)
    b8.place(x= (canvas_width / 3) + 1, y= 2 * (canvas_height / 3) + 1, width = (canvas_width / 3) - 2, height = (canvas_height / 3))
    b9.place(x= (2 * (canvas_width / 3)) + 1, y= (2 * (canvas_height / 3)) + 1, width = (canvas_width / 3), height = (canvas_height / 3))


def check_winner():
    global player
    
    if (game[0] != -1 and game[1] != -1 and game[2] != -1 and (game[0] + game[1] + game[2]) % 3 == 0 ):
        display_winner(0, 0, 0, 2)

    elif (game[3] != -1 and game[4] != -1 and game[5] != -1 and (game[3] + game[4] + game[5]) % 3 == 0 ):
        display_winner(1, 0, 1, 2)
        
    elif (game[6] != -1 and game[7] != -1 and game[8] != -1 and (game[6] + game[7] + game[8]) % 3 == 0 ):
        display_winner(2, 0, 2, 2)
        
    elif (game[0] != -1 and game[3] != -1 and game[6] != -1 and (game[0] + game[3] + game[6]) % 3 == 0 ):
        display_winner(0, 0, 2, 0)
            
    elif (game[1] != -1 and game[4] != -1 and game[7] != -1 and (game[1] + game[4] + game[7]) % 3 == 0 ):
        display_winner(0, 1, 2, 1)
            
    elif (game[2] != -1 and game[5] != -1 and game[8] != -1 and (game[2] + game[5] + game[8]) % 3 == 0 ):
        display_winner(0, 2, 2, 2)
            
    elif (game[0] != -1 and game[4] != -1 and game[8] != -1 and (game[0] + game[4] + game[8]) % 3 == 0 ):
        display_winner(0, 0, 2, 2)
            
    elif (game[2] != -1 and game[4] != -1 and game[6] != -1 and (game[2] + game[4] + game[6]) % 3 == 0 ):
            display_winner(0, 2, 2, 0)



    elif (click_count == 9):
        result = messagebox.askyesno("TIE!", f"No winner :(\n\nDo you want to play again?")
        if result:
            # Start a new game or reset the game state here
            root.destroy()
            os.startfile("tictactoe.py")
        else:
            # Close the application or take appropriate action
            root.destroy()
        
        
    else:
        player = 1 - player
    

def display_winner(row1, col1, row2, col2):
    global canvas, player

    player_char = "X"
    
    cell_width = canvas_width / 3
    cell_height = canvas_height / 3
    
    centre_x1 = col1 * cell_width + cell_width / 2
    centre_y1 = row1 * cell_height + cell_height / 2
    centre_x2 = col2 * cell_width + cell_width / 2
    centre_y2 = row2 * cell_height + cell_height / 2

    canvas.create_line(centre_x1, centre_y1, centre_x2, centre_y2, fill = "black", width = 5)

    
    if (player == 0):
        player_char = "O"
        
    result = messagebox.askyesno("WINNER!", f"Player {player_char} wins!\n\nDo you want to play again?")
    if result:
        # Start a new game or reset the game state here
        root.destroy()
        os.startfile("tictactoe.py")
    else:
    # Close the application or take appropriate action
        root.destroy()
    
   
def draw_x(row, col, s_width, s_height):
    global canvas
    cell_width = s_width / 3
    cell_height = s_height / 3

    # Calculate the center of the specified cell
    centre_x = col * cell_width + cell_width / 2
    centre_y = row * cell_height + cell_height / 2

    # Calculate the size of the X based on the cell dimensions
    x_size = min(cell_width, cell_height) * 0.4

    # Draw the X
    canvas.create_line(
        centre_x - x_size,
        centre_y - x_size,
        centre_x + x_size,
        centre_y + x_size,
        fill="yellow",
        width=2
    )
    canvas.create_line(
        centre_x - x_size,
        centre_y + x_size,
        centre_x + x_size,
        centre_y - x_size,
        fill="yellow",
        width=2
    )

def draw_o(row, col, s_width, s_height):
    global canvas
    
    cell_width = s_width / 3
    cell_height = s_height / 3

     # Calculate the center of the specified cell
    centre_x = col * cell_width + cell_width / 2
    centre_y = row * cell_height + cell_height / 2
    
    # Calculate the size of the oval based on the cell dimensions and a scaling factor
    scaling_factor = 0.9  # Adjust this value to control the size of the oval
    oval_width = cell_width * scaling_factor
    oval_height = cell_height * scaling_factor

  
    canvas.create_oval(
        centre_x - (oval_width / 2),
        centre_y - (oval_height / 2),
        centre_x + (oval_width / 2),
        centre_y + (oval_height / 2),
        outline="yellow",
        width=2
    )

def button_click(b, row, col):
    global game, player, click_count
    
    b.destroy()
    
    if(player == 0):
        draw_o(row, col, canvas_width, canvas_height)
        game[row * 3 + col] = 0
        click_count += 1

    else:
        draw_x(row, col, canvas_width, canvas_height)
        game[row * 3 + col] = 1
        click_count += 1
  
        
    check_winner()


    
    
# MAIN PROGRAM
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Tic Tac Toe")
    root.geometry("600x500")
    root.resizable(width=False, height=False)

    canvas = tk.Canvas(root, bg="light sky blue")
    canvas.grid(row=0, column=0, sticky="nsew")
    canvas.pack(fill=tk.BOTH, expand=True)

    canvas_width = 600
    canvas_height = 500

    draw_board(canvas, canvas_width, canvas_height)

    configure_game()


    tk.mainloop()

