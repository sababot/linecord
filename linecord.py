import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle
import time
import os
import sys
sys.path.insert(0, "./discord")
import messages as discord_messages
import servers as discord_servers
import channels as discord_channels

def init(w, max_height, max_width):
  w.addstr(round(max_height / 2) - 3, round(max_width / 2) - 14, "     _ _     _ _")
  w.addstr(round(max_height / 2) - 2, round(max_width / 2) - 14, "  __| (_)___| (_)_ __   ___")
  w.addstr(round(max_height / 2) - 1, round(max_width / 2) - 14, " / _` | / __| | | '_ \ / _ \ ")
  w.addstr(round(max_height / 2), round(max_width / 2) - 14, "| (_| | \__ | | | | | |  __/")
  w.addstr(round(max_height / 2) + 1, round(max_width / 2) - 14, " \__,_|_|___|_|_|_| |_|\___|")
  w.addstr(round(max_height / 2) + 2, round(max_width / 2) - 14, "                  by sababot")
  w.refresh()

class tui:
  def __init__(self):
    self.section_num = 2
    self.username = ""
    self.channels = None
    self.active_server = None
    self.active_server_member_count = None

  def home_panel(self, w, max_height, max_width, servers, token):
    w.nodelay(False)
    section = 0

    # INIT
    key = None

    # USER
    self.username = discord_messages.get_username(token)["username"]

    while 1:
      # LOGIC
      if key != None:
        if key == curses.KEY_UP and (section == 1 or section == 3):
          section -= 1
        elif key == curses.KEY_DOWN and (section == 0 or section == 2):
          section += 1

        elif key == curses.KEY_RIGHT and section == 0:
          section += 2
        elif key == curses.KEY_RIGHT and section == 1:
          section += 1
        elif key == curses.KEY_RIGHT and section == 2:
          section += 2
        elif key == curses.KEY_RIGHT and section == 3:
          section += 1

        elif key == curses.KEY_LEFT and (section == 2 or section == 4 or section == 3):
          section -= 2

        elif key in {curses.KEY_ENTER, 10, 13} and section == 0:
          self.section_num = 0
          break

      # CONTENT SERVERS
      for i, row in enumerate(servers):
        if self.active_server == i:
          w.attron(curses.color_pair(2))
          w.addstr(1 + i, 3, row['name'])
          w.attroff(curses.color_pair(2))
        else:
          w.addstr(1 + i, 3, row['name'])

      # CONTENT CHANNELS
      if self.channels != None:
        for i, channel in enumerate(self.channels):
          w.addstr(round(max_height / 2) + i, 3, channel['name'])

      # CONTENT MEMBERS
      if self.active_server_member_count != None:
        w.addstr(1, max_width - 19, "count: " + str(self.active_server_member_count))

      # RECTANGLES
      if section == 0:
        w.attron(curses.color_pair(2))
        rectangle(w, 0, 1, round(max_height / 2) - 1, 20)
        w.attroff(curses.color_pair(2))
        rectangle(w, 0, 21, max_height - 4, max_width - 21)
        rectangle(w, max_height - 3, 21, max_height - 1, max_width - 21)
        rectangle(w, 0, max_width - 20, max_height - 1, max_width - 2)
        rectangle(w, round(max_height / 2), 1, max_height - 1, 20)

      elif section == 1:
        w.attron(curses.color_pair(2))
        rectangle(w, round(max_height / 2), 1, max_height - 1, 20)
        w.attroff(curses.color_pair(2))
        rectangle(w, 0, 1, round(max_height / 2) - 1, 20)
        rectangle(w, 0, 21, max_height - 4, max_width - 21)
        rectangle(w, max_height - 3, 21, max_height - 1, max_width - 21)
        rectangle(w, 0, max_width - 20, max_height - 1, max_width - 2)

      elif section == 2:
        w.attron(curses.color_pair(2))
        rectangle(w, 0, 21, max_height - 4, max_width - 21)
        w.attroff(curses.color_pair(2))
        rectangle(w, 0, 1, round(max_height / 2) - 1, 20)
        rectangle(w, max_height - 3, 21, max_height - 1, max_width - 21)
        rectangle(w, 0, max_width - 20, max_height - 1, max_width - 2)
        rectangle(w, round(max_height / 2), 1, max_height - 1, 20)

      elif section == 3:
        w.attron(curses.color_pair(2))
        rectangle(w, max_height - 3, 21, max_height - 1, max_width - 21)
        w.attroff(curses.color_pair(1))
        rectangle(w, 0, 1, round(max_height / 2) - 1, 20)
        rectangle(w, 0, 21, max_height - 4, max_width - 21)
        rectangle(w, 0, max_width - 20, max_height - 1, max_width - 2)
        rectangle(w, round(max_height / 2), 1, max_height - 1, 20)

      elif section == 4:
        w.attron(curses.color_pair(2))
        rectangle(w, 0, max_width - 20, max_height - 1, max_width - 2)
        w.attroff(curses.color_pair(2))
        rectangle(w, 0, 1, round(max_height / 2) - 1, 20)
        rectangle(w, 0, 21, max_height - 4, max_width - 21)
        rectangle(w, max_height - 3, 21, max_height - 1, max_width - 21)
        rectangle(w, round(max_height / 2), 1, max_height - 1, 20)

      # TEXT
      w.addstr(0, 2, "servers")
      w.addstr(round(max_height / 2), 2, "channels")
      w.addstr(0, max_width - 19, "members")
      w.addstr(0, 22, "messages")
      w.addstr(0, round(max_width / 2) - 6, "disline v0.1")

      key = w.getch()

  def servers_panel(self, w, token, max_height, max_width, servers):
    index = 0
    clear = False
    w.nodelay(True)

    while 1:
      try:
        key = w.getch()

      except:
        key = ""

      if key == curses.KEY_UP and index > 0:
        index -= 1

      elif key == curses.KEY_DOWN and index < len(servers) - 1:
        index += 1

      elif key == 27:
        break

      elif key in {curses.KEY_ENTER, 10, 13}:
        clear = False
        self.channels = discord_channels.get_channels(token, servers[index]["id"])
        self.active_server_member_count = discord_servers.get_members(token, servers[index]["id"])
        self.active_server = index

      # SERVER
      w.attron(curses.color_pair(2))
      rectangle(w, 0, 1, round(max_height / 2) - 1, 20)
      w.attroff(curses.color_pair(2))
      w.addstr(0, 2, "servers")
      for i, row in enumerate(servers):
        if i == index:
          w.attron(curses.color_pair(3))
          w.addstr(1 + i, 3, row['name'])
          w.attroff(curses.color_pair(3))

        else:
          if self.active_server == i:
            w.attron(curses.color_pair(2))
            w.addstr(1 + i, 3, row['name'])
            w.attroff(curses.color_pair(2))
          else:
            w.addstr(1 + i, 3, row['name'])

      # CONTENT CHANNELS
      if self.channels != None:
        if clear == False:
          w.clear()
          clear = True
        for i, channel in enumerate(self.channels):
          w.addstr(round(max_height / 2) + i, 3, channel['name'])

      # CONTENT MEMBERS
      if self.active_server_member_count != None:
        w.addstr(1, max_width - 19, "count: " + str(self.active_server_member_count))

      # CHANNELS
      rectangle(w, round(max_height / 2), 1, max_height - 1, 20)
      w.addstr(round(max_height / 2), 2, "channels")

      # CONTENT
      rectangle(w, 0, 21, max_height - 4, max_width - 21)
      w.addstr(0, 22, "messages")
      
      # INPUT
      rectangle(w, max_height - 3, 21, max_height - 1, max_width - 21)
      
      # MEMBERS
      rectangle(w, 0, max_width - 20, max_height - 1, max_width - 2)
      w.addstr(0, max_width - 19, "members")

      w.addstr(0, round(max_width / 2) - 6, "disline v0.1")

      w.refresh()

def main(w):
  # DISCORD VARIABLES
  token = "MzU4MzM3OTgxMjk3NDU5MjAx.GUVsqK.2_WkGNCho310ol9mOLIgZyERRoYGd-y8vVmZkg"

  # COLOURS
  curses.init_pair(1, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
  curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLACK)
  curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)

  # MENU CONFIG
  max_height, max_width = w.getmaxyx()
  curses.curs_set(0)

  # MAIN LOOP
  init(w, max_height, max_width)
  time.sleep(1)
  w.clear()
  servers_list = discord_servers.get_servers(token)
  tui_object = tui()

  while 1:
    tui_object.home_panel(w, max_height, max_width, servers_list, token)

    if tui_object.section_num == 0:
      tui_object.servers_panel(w, token, max_height, max_width, servers_list)

  w.refresh()
  w.getch()

os.environ.setdefault('ESCDELAY', '0')
wrapper(main)