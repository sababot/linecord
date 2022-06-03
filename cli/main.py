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

class sections:
  def __init__(self, servers, content, messages, users):
    self.servers = servers
    self.content = content
    self.messages = messages
    self.users = users

    self.section_num = 2

  def draw(self, w, max_height, max_width, servers):
    w.nodelay(False)
    section = 0

    # INIT
    # RECTANGLES
    if section == 0:
      w.attron(curses.color_pair(2))
      rectangle(w, 1, 1, max_height - 2, 20)
      w.attroff(curses.color_pair(2))
      rectangle(w, 1, 21, max_height - 5, max_width - 21)
      rectangle(w, max_height - 4, 21, max_height - 2, max_width - 21)
      rectangle(w, 1, max_width - 20, max_height - 2, max_width - 2)

    elif section == 1:
      w.attron(curses.color_pair(2))
      rectangle(w, 1, 21, max_height - 5, max_width - 21)
      w.attroff(curses.color_pair(2))
      rectangle(w, 1, 1, max_height - 2, 20)
      rectangle(w, max_height - 4, 21, max_height - 2, max_width - 21)
      rectangle(w, 1, max_width - 20, max_height - 2, max_width - 2)

    elif section == 2:
      w.attron(curses.color_pair(2))
      rectangle(w, max_height - 4, 21, max_height - 2, max_width - 21)
      w.attroff(curses.color_pair(2))
      rectangle(w, 1, 1, max_height - 2, 20)
      rectangle(w, 1, 21, max_height - 5, max_width - 21)
      rectangle(w, 1, max_width - 20, max_height - 2, max_width - 2)

    elif section == 3:
      w.attron(curses.color_pair(2))
      rectangle(w, 1, max_width - 20, max_height - 2, max_width - 2)
      w.attroff(curses.color_pair(2))
      rectangle(w, 1, 1, max_height - 2, 20)
      rectangle(w, 1, 21, max_height - 5, max_width - 21)
      rectangle(w, max_height - 4, 21, max_height - 2, max_width - 21)

    # SERVER
    for i, row in enumerate(servers):
      w.addstr(2 + i, 3, row)

    while 1:
      key = w.getch()
      w.clear()

      # LOGIC
      if key == curses.KEY_UP and section == 2:
        section -= 1
      elif key == curses.KEY_DOWN and section == 1:
        section += 1

      elif key == curses.KEY_RIGHT and section == 1:
        section += 2
      elif key == curses.KEY_RIGHT and section != 1 and section != 3:
        section += 1

      elif key == curses.KEY_LEFT and section == 2:
        section -= 2
      elif key == curses.KEY_LEFT and section == 3:
        section -= 2
      elif key == curses.KEY_LEFT and section != 2 and section != 0:
        section -= 1

      elif key == 27 and section == 0:
        self.section_num = 0
        break

      # RECTANGLES
      if section == 0:
        w.attron(curses.color_pair(2))
        rectangle(w, 1, 1, max_height - 2, 20)
        w.attroff(curses.color_pair(2))
        rectangle(w, 1, 21, max_height - 5, max_width - 21)
        rectangle(w, max_height - 4, 21, max_height - 2, max_width - 21)
        rectangle(w, 1, max_width - 20, max_height - 2, max_width - 2)

      elif section == 1:
        w.attron(curses.color_pair(2))
        rectangle(w, 1, 21, max_height - 5, max_width - 21)
        w.attroff(curses.color_pair(2))
        rectangle(w, 1, 1, max_height - 2, 20)
        rectangle(w, max_height - 4, 21, max_height - 2, max_width - 21)
        rectangle(w, 1, max_width - 20, max_height - 2, max_width - 2)

      elif section == 2:
        w.attron(curses.color_pair(2))
        rectangle(w, max_height - 4, 21, max_height - 2, max_width - 21)
        w.attroff(curses.color_pair(2))
        rectangle(w, 1, 1, max_height - 2, 20)
        rectangle(w, 1, 21, max_height - 5, max_width - 21)
        rectangle(w, 1, max_width - 20, max_height - 2, max_width - 2)

      elif section == 3:
        w.attron(curses.color_pair(2))
        rectangle(w, 1, max_width - 20, max_height - 2, max_width - 2)
        w.attroff(curses.color_pair(2))
        rectangle(w, 1, 1, max_height - 2, 20)
        rectangle(w, 1, 21, max_height - 5, max_width - 21)
        rectangle(w, max_height - 4, 21, max_height - 2, max_width - 21)

      # SERVER
      for i, row in enumerate(servers):
        w.addstr(2 + i, 3, row)

      w.refresh()

  def servers_func(self, w, max_height, max_width, servers):
    index = 0

    w.nodelay(True)
    w.attron(curses.color_pair(2))
    rectangle(w, 1, 1, max_height - 2, 20)
    w.attroff(curses.color_pair(2))
    for i, row in enumerate(servers):
      if i == index:
        w.attron(curses.color_pair(3))
        w.addstr(2 + i, 3, row)
        w.attroff(curses.color_pair(3))

      else:
        w.addstr(2 + i, 3, row)

    rectangle(w, 1, 21, max_height - 5, max_width - 21)
    rectangle(w, max_height - 4, 21, max_height - 2, max_width - 21)
    rectangle(w, 1, max_width - 20, max_height - 2, max_width - 2)

    while 1:
      try:
        key = w.getch()

      except:
        key = ""

      if key == curses.KEY_UP:
        index -= 1

      elif key == curses.KEY_DOWN:
        index += 1

      elif key == 27:
        break

      w.attron(curses.color_pair(2))
      rectangle(w, 1, 1, max_height - 2, 20)
      w.attroff(curses.color_pair(2))
      for i, row in enumerate(servers):
        if i == index:
          w.attron(curses.color_pair(3))
          w.addstr(2 + i, 3, row)
          w.attroff(curses.color_pair(3))

        else:
          w.addstr(2 + i, 3, row)

      rectangle(w, 1, 21, max_height - 5, max_width - 21)
      rectangle(w, max_height - 4, 21, max_height - 2, max_width - 21)
      rectangle(w, 1, max_width - 20, max_height - 2, max_width - 2)

      w.refresh()

def main(w):
  # COLOURS
  curses.init_pair(1, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
  curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLACK)
  curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)

  # VARIABLES
  max_height, max_width = w.getmaxyx()

  servers = curses.newwin(max_height - 4, 18, 2, 2)
  content = curses.newwin(max_height - 7, max_width - 43, 2, 22)
  messages = curses.newwin(1, max_width - 43, max_height - 3, 22)
  users = curses.newwin(max_height - 4, 17, 2, max_width - 19)

  # MAIN LOOP
  servers_list = ['loopwhole', 'sabaworld', 'pussypalace']
  curses.curs_set(0)
  sections_object = sections(servers, content, messages, users)

  while 1:
    sections_object.draw(w, max_height, max_width, servers_list)

    if sections_object.section_num == 0:
      sections_object.servers_func(w, max_height, max_width, servers_list)

  w.refresh()
  w.getch()

wrapper(main)