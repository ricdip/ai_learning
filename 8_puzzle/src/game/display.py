import curses
import signal
import sys

class Display:
    def __init__(self):
        self.__scr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        curses.start_color()
        signal.signal(signal.SIGINT, self.__sig_handler)

    def redraw(self, grid):
        self.__scr.clear()

        self.__draw_grid(grid)

        self.__scr.refresh()

    def __draw_grid(self, grid):
        self.__scr.addstr(" GRID\n\n")
        for row in grid:
            for col in row:
                self.__scr.addstr(" {} ".format(col))
            self.__scr.addstr("\n")
        self.__scr.addstr("\n")


    def __sig_handler(self, signal, frame):
        self.__exit()


    def __exit(self):
        curses.echo()
        curses.nocbreak()
        curses.endwin()
        sys,exit(0)
