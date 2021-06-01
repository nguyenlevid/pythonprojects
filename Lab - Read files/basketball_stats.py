'''
This program produces basketball stats for a team including the
team's average points per game, the team's total points for each
game, and after accepting input of one player's number, this player's
maximum points in any one game.

The data for the program is in a file where each line gives the
points earned by each player for one game.

    
'''

def get_int_num(prompt, low_num, high_num):
    '''
    prompts a user for integer input until the value entered
    in a specified range.
    
    Params:
    prompt (str): the words used to prompt the user for input
    low_num (int): the smallest integer accepted as valid
    high_num (int): the largest integer accepted as valid
    
    Returns:
    the valid integer entered by the user
    '''
    num = int(input(prompt))
    while num < low_num or num > high_num:
        print('Invalid, Try again.')
        num = int(input(prompt))
    return num

def get_data(filename):
    '''
    This function reads the points earned by each player in each game.
    
    Param:
    filename (str): the filename with the data
    
    Returns:
    a 2D list of points where each row represents one game and each
    column represents data for one player
    '''
    f_in = open(filename, 'r')
    points = []
    for line in f_in:
        one_game = line.split()
        one_int_game = [int(score) for score in one_game]
        points.append(one_int_game)
    return points
        
        
def print_table(points):
    '''
    prints a nicely aligned table of points with headers for the player number
    and game number
    
    Params:
    points (2D list): a 2D list of points where each row represents one game and each
    column represents data for one player
    '''
    header = 'Player'
    print(' ' * 6, end = '')
    for playerNum in range(len(points[0])):
        print(f'{header:>8} {playerNum}', end = '')
    print()
    for gameNum in range(len(points)):
        print(f'Game {gameNum}{points[gameNum][0]:8}', end = '')
        for playerNum in range(1, len(points[gameNum])):
            print(f'{points[gameNum][playerNum]:10}', end = '')
        print()

def get_team_average(points):
    '''
    computes the average number of points per game for the team
    
    Params:
    points (2D list): a 2D list of points where each row represents one game and each
    column represents data for one player
    
    Returns:
    the average number of points per game for the team
    '''
    sum_score = 0
    num_game = len(points)
    for part in points:
        for element in part:
            sum_score += element
    average = sum_score/num_game
    print(f"Team's average points per game is {average:.2f}")

def get_game_total(points, gameNum):
    '''
    computes the total number of points scored by the team in one game
    
    Params:
    points (2D list): a 2D list of points where each row represents one game and each
    column represents data for one player
    
    Returns:
    the total number of points scored by the team in one game
    '''
    total_score = 0
    for score in points[gameNum]:
        total_score += score
    return total_score

def print_game_points(points):
    '''
    prints a table with each game number and the total points scored in that game
    
    Params:
    points (2D list): a 2D list of points where each row represents one game and each
    column represents data for one player
    '''
    print('Game   Points')
    for gameNum in range(len(points)):
        game_total = get_game_total(points, gameNum)
        print(' ', gameNum, '    ', game_total)
        
def max_player_points(points, player_num):
    '''
    calculates the maximum points earned by one player in any one game
    
    Params:
    points (2D list): a 2D list of points where each row represents one game and each
    column represents data for one player
    player_num (int): the player number whose maximum is desired
    
    Returns:
    the maximum points in any one game by the desired player
    '''
    max_point = float('-inf')
    for game in range(len(points)):
        point = points[game][player_num]
        if point > max_point:
            max_point = point
    print(f"Player {player_num}'s max points in one game is {max_point}")

def main():
    # ask user for the file name and print the table of points per game per player
    filename = input('Enter filename: ')
    points = get_data(filename)
    print()
    print_table(points)
    print()
    print()
    # Add your code to the main function here
    get_data(filename)
    get_team_average(points)
    print()
    print_game_points(points)
    print()
    prompt = "Enter player number: "
    low_num = 0
    high_num = len(points[0]) - 1
    player_num = get_int_num(prompt, low_num, high_num)
    max_player_points(points, player_num)
main()        