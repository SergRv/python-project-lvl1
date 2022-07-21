#!/usr/bin/env python
from brain_games import start_game
from brain_games.games.even import start_round
from brain_games.games.even import get_quest


def main():
    start_game.play_game(get_quest, start_round)


if __name__ == '__main__':
    main()
