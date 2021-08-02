from game import PianoMoverRepresentation


def main():
    r = PianoMoverRepresentation()
    r.print_grid()
    print()
    print("move up")
    r2 = r.blocks["1_1"].move_up()
    print()
    r2.print_grid()
    print("move down")
    r2 = r.blocks["1_1"].move_down()
    print()
    r2.print_grid()
    print("move left")
    r2 = r.blocks["1_1"].move_left()
    print()
    r2.print_grid()
    print("move right")
    r2 = r.blocks["1_1"].move_right()
    print()
    r2.print_grid()


if __name__ == "__main__":
    main()
