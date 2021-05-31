from game import Game

def main():
    g = Game(random_grid=False, watch_moves=False, output=True)
    g.start()


if __name__ == '__main__':
    main()
