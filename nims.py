import sys

def nimsGame():
    player_one, player_two = game_setup()
    current_player = player_one
    stones_count = 20
    player_pick = 0

    while stones_count > 0:
        print '{player}\'s turn'.format(
            player=current_player
        )

        while not (0 < int(player_pick) < 4):
            player_pick = raw_input('How many stones do you want to take? Remember to only take between 1 and 3\t')

        stones_count -= int(player_pick)

        print 'there are {stone_count} left'.format(
            stone_count=stones_count
        )

        if check_for_win(stones_count, current_player) is False:
            current_player = set_current_player(current_player, player_one, player_two)
            player_pick = 0


def check_for_win(stones_count, current_player):
    if stones_count == 0:
        print '~~~~~~~{player}  wins! Game Over~~~~~~~'.format(
            player=current_player
        )
    else:
        return False


def set_current_player(current_player, player_one, player_two):
    if current_player == player_one:
        return player_two

    return player_one

def game_setup():
    print 'Hello, lets play a game of nims assignment. Two players have 20 stones in front of them. They can pick up between 1 and 3 stones. The last player to pick up the last stone wins'

    player_one = raw_input('Player one - what is your name?\t' )
    player_two = raw_input('Player two - what is your name?\t' )

    print 'Great! Let\'s start the game {player_one} and {player_two}'.format(
        player_one=player_one,
        player_two=player_two
    )

    return (player_one, player_two)

if __name__ == '__main__':
    nimsGame()
