import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle
import time

def init(w):
  w.addstr("     _ _     _ _\n")
  w.addstr("  __| (_)___| (_)_ __   ___\n")
  w.addstr(" / _` | / __| | | '_ \ / _ \ \n")
  w.addstr("| (_| | \__ | | | | | |  __/\n")
  w.addstr(" \__,_|_|___|_|_|_| |_|\___|\n")

def main(w):
  curses.curs_set(0)
  max_height, max_width = w.getmaxyx()
  typing = False

  # SERVERS
  servers = curses.newwin(max_height - 4, 18, 2, 2)
  servers_box = Textbox(servers)
  rectangle(w, 1, 1, max_height - 2, 20)

  # CONTENT
  content = curses.newwin(max_height - 7, max_width - 43, 2, 22)
  content_box = Textbox(content)
  rectangle(w, 1, 21, max_height - 5, max_width - 21)

  # MESSAGE
  message = curses.newwin(1, max_width - 43, max_height - 3, 22)
  message_box = Textbox(message)
  rectangle(w, max_height - 4, 21, max_height - 2, max_width - 21)

  # USERS
  users = curses.newwin(max_height - 4, 17, 2, max_width - 19)
  users_box = Textbox(users)
  rectangle(w, 1, max_width - 20, max_height - 2, max_width - 2)

  w.refresh()

  w.getch()

wrapper(main)