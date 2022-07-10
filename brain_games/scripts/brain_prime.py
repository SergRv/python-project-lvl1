#!/usr/bin/env python
from brain_games.games import start_game
from brain_games.games.isprime import counted
from brain_games.games.isprime import get_quest


def main():
    start_game.started_game(get_quest, counted)


if __name__ == '__main__':
    main()