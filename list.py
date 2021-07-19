#!/usr/bin/env python3

def main():
    game = ['game', 'cricket', 'football', 'satya']
    print(game[1])
    # Below is search satya in game and return index
    i = game.index('satya')
    print(game[i])
    # List we can modify
    game.append('Sundar')
    # Insert at begining
    game.insert(0,'Sahu')
    # We can remove
    #game.remove('football')
    # remove using pop
    game.pop()
    #del game[0]
    print_list(game)

def print_list(game):
    for i in game:
        #print(i, end='', flush=True)
        print(i)
        print()

if __name__ == '__main__':main()
