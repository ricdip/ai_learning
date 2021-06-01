import signal
import sys

class Display:
    def __init__(self, output=True):
        self.output = output
        signal.signal(signal.SIGINT, self.__sig_handler)

    def draw_state(self, state, move_number):
        if self.output:
            print(" - MOVE {}\n\n".format(move_number))
            for row in state.representation.grid:
                for col in row:
                    print(" {} ".format(col), end='')
                print("\n")
            print("\n")

    def print_status(self, iterations):
        if self.output:
            print(" - Iterations: {}".format(iterations), end='\r')

    def print_success(self):
        if self.output:
            print("\n")
            print(" SOLUTION FOUND\n")

    def print_infos(self, infos):
        if self.output:
            for k in infos.keys():
                print("- {}: {}".format(k, infos[k]))

    def __sig_handler(self, signal, frame):
        self.__exit()

    def __exit(self):
        if self.output:
            print("")
            print("Exiting")
        sys.exit(0)
