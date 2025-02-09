import random
li = ['_', '_', '_', '_', '_', '_', '_', '_', '_']

def pattern():
    for i in range(3):
        print(li[i*3:(i+1)*3])
    print('')
pattern()

player_turn = True
computer_turn = False

def check_winner(symbol):
    for i in range(0, 9, 3):
        if li[i] == li[i+1] == li[i+2] == symbol:  
            return True
    for i in range(3):
        if li[i] == li[i+3] == li[i+6] == symbol:  
            return True
    if li[0] == li[4] == li[8] == symbol:  
        return True
    if li[2] == li[4] == li[6] == symbol: 
        return True
    return False

def is_board_full():
    return all([spot != '_' for spot in li])

while li.count('_') > 0:
    if player_turn:
        index = int(input("Player Turn: Enter the index position between 0 to 8 to write your symbol 'X': "))
        if 0 <= index <= 8:
            if li[index] == '_':
                li[index] = 'X'
                pattern()
                if check_winner('X'):
                    print("Player wins!")
                    break
                player_turn = False
                computer_turn = True
            else:
                print("Space is already taken, try again.")
        else:
            print("Please enter a valid index between 0 and 8.")

    elif computer_turn:
        index = random.randint(0, 8)
        while li[index] != '_':
            index = random.randint(0, 8)
        li[index] = 'O'
        pattern()
        print(f"Computer chose index {index}")
        if check_winner('O'):
            print("Computer wins!")
            break
        computer_turn = False
        player_turn = True

    if is_board_full():
        print("It's a tie!")
        break
