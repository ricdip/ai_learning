import signal
import sys

class Display:
    def __init__(self):
        signal.signal(signal.SIGINT, self.__sig_handler)

    def draw_state(self, state, move_number):
        print(" - MOVE {}\n\n".format(move_number))
        for row in state.representation.grid:
            for col in row:
                print(" {} ".format(col), end='')
            print("\n")
        print("\n")

    def print_status(self, iterations):
        print(" - Iterations: {}".format(iterations), end='\r')

    def print_success(self):
        print("\n")
        print(" SOLUTION FOUND\n")

    def print_infos(self, infos):
        for k in infos.keys():
            print("- {}: {}".format(k, infos[k]))

    def __sig_handler(self, signal, frame):
        self.__exit()

    def __exit(self):
        print("")
        print("Exiting")
        sys.exit(0)
