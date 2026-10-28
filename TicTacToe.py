
import tkinter

# Check a tile click
def set_tile(row, column):
    global curr_player

    if game_over:
        return

    # Prevent clicking an occupied tile
    if board[row][column]["text"] != "":
        return

    # Place the current player's mark
    board[row][column]["text"] = curr_player

    # Check for a winner or tie
    check_winner()

    if game_over:
        return

    # Switch player
    if curr_player == playerX:
        curr_player = player0
    else:
        curr_player = playerX

    label.config(text=curr_player + "'s turn")


def check_winner():
    global turns, game_over

    turns += 1

    # Check horizontal rows
    for row in range(3):
        if (board[row][0]["text"] ==
            board[row][1]["text"] ==
            board[row][2]["text"] != ""):

            label.config(
                text=board[row][0]["text"] + " is the winner!",
                foreground=color_yellow
            )

            for column in range(3):
                board[row][column].config(
                    foreground=color_yellow,
                    background=color_light_gray
                )

            game_over = True
            return

    # Check vertical columns
    for column in range(3):
        if (board[0][column]["text"] ==
            board[1][column]["text"] ==
            board[2][column]["text"] != ""):

            label.config(
                text=board[0][column]["text"] + " is the winner!",
                foreground=color_yellow
            )

            for row in range(3):
                board[row][column].config(
                    foreground=color_yellow,
                    background=color_light_gray
                )

            game_over = True
            return

    # Check main diagonal
    if (board[0][0]["text"] ==
        board[1][1]["text"] ==
        board[2][2]["text"] != ""):

        label.config(
            text=board[0][0]["text"] + " is the winner!",
            foreground=color_yellow
        )

        for i in range(3):
            board[i][i].config(
                foreground=color_yellow,
                background=color_light_gray
            )

        game_over = True
        return

    # Check opposite diagonal
    if (board[0][2]["text"] ==
        board[1][1]["text"] ==
        board[2][0]["text"] != ""):

        label.config(
            text=board[0][2]["text"] + " is the winner!",
            foreground=color_yellow
        )

        board[0][2].config(
            foreground=color_yellow,
            background=color_light_gray
        )
        board[1][1].config(
            foreground=color_yellow,
            background=color_light_gray
        )
        board[2][0].config(
            foreground=color_yellow,
            background=color_light_gray
        )

        game_over = True
        return

    # Check for a tie
    if turns == 9:
        game_over = True
        label.config(text="It's a Tie!", foreground=color_yellow)


def new_game():
    global turns, game_over, curr_player

    turns = 0
    game_over = False
    curr_player = playerX

    label.config(
        text=curr_player + "'s turn",
        foreground="white"
    )

    # Clear every tile
    for row in range(3):
        for column in range(3):
            board[row][column].config(
                text="",
                foreground=color_blue,
                background=color_gray
            )


# Game settings
playerX = "X"
player0 = "O"
curr_player = playerX

board = [[None for _ in range(3)] for _ in range(3)]

color_blue = "#4584b6"
color_yellow = "#ffde57"
color_gray = "#343434"
color_light_gray = "#646464"

turns = 0
game_over = False

# Create the window
window = tkinter.Tk()
window.title("Tic Tac Toe")
window.resizable(False, False)
window.configure(background=color_gray)

# Create the game frame
frame = tkinter.Frame(window, background=color_gray)

label = tkinter.Label(
    frame,
    text=curr_player + "'s turn",
    font=("Consolas", 20),
    background=color_gray,
    foreground="white"
)
label.grid(row=0, column=0, columnspan=3, sticky="we")

# Create the 3x3 game board
for row in range(3):
    for column in range(3):
        board[row][column] = tkinter.Button(
            frame,
            text="",
            font=("Consolas", 50, "bold"),
            background=color_gray,
            foreground=color_blue,
            width=4,
            height=1,
            command=lambda r=row, c=column: set_tile(r, c)
        )
        board[row][column].grid(row=row + 1, column=column)

# Restart button
restart_button = tkinter.Button(
    frame,
    text="Restart",
    font=("Consolas", 20),
    background=color_gray,
    foreground="white",
    command=new_game
)
restart_button.grid(row=4, column=0, columnspan=3, sticky="we")

frame.pack()

# Center the window on the screen
window.update_idletasks()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = (screen_width - window_width) // 2
window_y = (screen_height - window_height) // 2

window.geometry(
    f"{window_width}x{window_height}+{window_x}+{window_y}"
)

# Start the game
window.mainloop()
