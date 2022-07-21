#!/usr/bin/env python
from brain_games import start_game
from brain_games.games.calc import get_quest
from brain_games.games.calc import start_round


def main():
    start_game.play_game(get_quest, start_round)


if __name__ == '__main__':
    main()
