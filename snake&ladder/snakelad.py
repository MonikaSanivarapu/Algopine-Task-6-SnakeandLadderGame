import random

def print_board(player1, player2):
    print(f"Player 1 is at position {player1}")
    print(f"Player 2 is at position {player2}")

def roll_die():
    return random.randint(1, 6)

def snake_ladder(position):
    snakes_and_ladders = {
        16: 6,
        47: 26,
        49: 11,
        56: 53,
        62: 19,
        64: 60,
        87: 24,
        93: 73,
        95: 75,
        98: 78
    }

    if position in snakes_and_ladders:
        new_position = snakes_and_ladders[position]
        if position > new_position:
            print(f"Oops! Snake at {position}. Player goes down to {new_position}")
        else:
            print(f"Yay! Ladder at {position}. Player climbs up to {new_position}")
        return new_position
    else:
        return position

def snake_and_ladder_game():
    player1_position = 1
    player2_position = 1

    while True:
        input("Player 1 - Press Enter to roll the die...")
        player1_roll = roll_die()
        player1_position += player1_roll
        player1_position = snake_ladder(player1_position)

        print_board(player1_position, player2_position)

        if player1_position >= 100:
            print("Player 1 wins!")
            break

        input("Player 2 - Press Enter to roll the die...")
        player2_roll = roll_die()
        player2_position += player2_roll
        player2_position = snake_ladder(player2_position)

        print_board(player1_position, player2_position)

        if player2_position >= 100:
            print("Player 2 wins!")
            break

snake_and_ladder_game()
