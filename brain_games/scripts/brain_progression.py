#!/usr/bin/env python
from brain_games import Start_game
from brain_games.games.progression import get_quest
from brain_games.games.progression import start_round


def main():
    Start_game.start_game(get_quest, start_round)


if __name__ == '__main__':
    main()
