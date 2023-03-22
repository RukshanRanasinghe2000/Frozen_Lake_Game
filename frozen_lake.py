board = [['S', 'F', 'F', 'F'],
         ['F', 'H', 'F', 'H'],
         ['F', 'F', 'F', 'H'],
         ['H', 'F', 'F', 'G']]


player_row, player_col = 0, 0

rewards = {'S': 0, 'F': 0, 'H': -1, 'G': 1}

actions = ['1', '2', '3', '4']


def choose_action():
    # return random.choice(actions)
    return str(input("UP ->1\tDOWN ->2\tLeft ->3\tRight ->4 \n\nEnter your choice : "))


# Define a function to take a step in the game
def take_step(action):
    global player_row, player_col
    if action == '1':
        if player_row > 0:
            player_row -= 1
    elif action == '2':
        if player_row < 3:
            player_row += 1
    elif action == '3':
        if player_col > 0:
            player_col -= 1
    elif action == '4':
        if player_col < 3:
            player_col += 1


def draw_board():
    for row in range(len(board)):
        for col in range(len(board[row])):
            if row == player_row and col == player_col:
                print('X', end=' ')
            else:
                print(board[row][col], end=' ')
        print()
    print()


def playGame():
    global player_row, player_col
    player_row, player_col = 0, 0
    while True:
        draw_board()
        action = choose_action()
        print(action)
        take_step(action)
        cell_type = board[player_row][player_col]
        print(cell_type)
        reward = rewards[cell_type]
        print(reward)
        if cell_type in ['H', 'G']:
            if cell_type == 'H':
                print("....You lost....")
            if cell_type == 'G':
                print("....You Won the Game....")
            draw_board()
            print("....END....")
            break



playGame()
