import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle
import time
import os
import sys
sys.path.insert(0, "/Users/aitorgh/Desktop/projects/programming/projects/disline/discord")
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

class sections:
  def __init__(self, servers, content, messages, users):
    self.servers = servers
    self.content = content
    self.messages = messages
    self.users = users

    self.section_num = 2
    self.username = ""
    self.channels = None
    self.active_server = None

  def draw(self, w, max_height, max_width, servers, token):
    w.nodelay(False)
    section = 0

    # INIT
    # USER
    self.username = discord_messages.get_username(token)["username"]

    # CONTENT SERVERS
    for i, row in enumerate(servers):
      if self.active_server == i:
        w.attron(curses.color_pair(2))
        w.addstr(2 + i, 3, row['name'])
        w.attroff(curses.color_pair(2))
      else:
        w.addstr(2 + i, 3, row['name'])

    # CONTENT CHANNELS
    if self.channels != None:
      for i, channel in enumerate(self.channels):
        w.addstr(round(max_height / 2) + i, 3, channel['name'])

    # RECTANGLES
    if section == 0:
      w.attron(curses.color_pair(2))
      rectangle(w, 1, 1, round(max_height / 2) - 2, 20)
      w.attroff(curses.color_pair(2))
      rectangle(w, 1, 21, max_height - 5, max_width - 21)
      rectangle(w, max_height - 4, 21, max_height - 2, max_width - 21)
      rectangle(w, 1, max_width - 20, max_height - 2, max_width - 2)
      rectangle(w, round(max_height / 2) - 1, 1, max_height - 2, 20)

    elif section == 1:
      w.attron(curses.color_pair(2))
      rectangle(w, round(max_height / 2) - 1, 1, max_height - 2, 20)
      w.attroff(curses.color_pair(2))
      rectangle(w, 1, 1, round(max_height / 2) - 2, 20)
      rectangle(w, 1, 21, max_height - 5, max_width - 21)
      rectangle(w, max_height - 4, 21, max_height - 2, max_width - 21)
      rectangle(w, 1, max_width - 20, max_height - 2, max_width - 2)

    elif section == 2:
      w.attron(curses.color_pair(2))
      rectangle(w, 1, 21, max_height - 5, max_width - 21)
      w.attroff(curses.color_pair(2))
      rectangle(w, 1, 1, round(max_height / 2) - 2, 20)
      rectangle(w, max_height - 4, 21, max_height - 2, max_width - 21)
      rectangle(w, 1, max_width - 20, max_height - 2, max_width - 2)
      rectangle(w, round(max_height / 2) - 1, 1, max_height - 2, 20)

    elif section == 3:
      w.attron(curses.color_pair(2))
      rectangle(w, max_height - 4, 21, max_height - 2, max_width - 21)
      w.attroff(curses.color_pair(2))
      rectangle(w, 1, 1, round(max_height / 2) - 2, 20)
      rectangle(w, 1, 21, max_height - 5, max_width - 21)
      rectangle(w, 1, max_width - 20, max_height - 2, max_width - 2)
      rectangle(w, round(max_height / 2) - 1, 1, max_height - 2, 20)

    elif section == 4:
      w.attron(curses.color_pair(2))
      rectangle(w, 1, max_width - 20, max_height - 2, max_width - 2)
      w.attroff(curses.color_pair(2))
      rectangle(w, 1, 1, round(max_height / 2) - 2, 20)
      rectangle(w, 1, 21, max_height - 5, max_width - 21)
      rectangle(w, max_height - 4, 21, max_height - 2, max_width - 21)
      rectangle(w, round(max_height / 2) - 1, 1, max_height - 2, 20)

    # TEXT
    w.addstr(1, 2, "servers")
    w.addstr(round(max_height / 2) - 1, 2, "channels")
    w.addstr(1, max_width - 19, "members")
    w.addstr(1, 22, "messages")
    w.addstr(0, round(max_width / 2) - 6, "disline v0.1")
    w.addstr(max_height - 1, round(max_width / 2) - (3 + round(len(self.username) / 2)), "user: " + self.username)

    while 1:
      key = w.getch()


      # LOGIC
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
          w.addstr(2 + i, 3, row['name'])
          w.attroff(curses.color_pair(2))
        else:
          w.addstr(2 + i, 3, row['name'])

      # CONTENT CHANNELS
      if self.channels != None:
        for i, channel in enumerate(self.channels):
          w.addstr(round(max_height / 2) + i, 3, channel['name'])

      # RECTANGLES
      if section == 0:
        w.attron(curses.color_pair(2))
        rectangle(w, 1, 1, round(max_height / 2) - 2, 20)
        w.attroff(curses.color_pair(2))
        rectangle(w, 1, 21, max_height - 5, max_width - 21)
        rectangle(w, max_height - 4, 21, max_height - 2, max_width - 21)
        rectangle(w, 1, max_width - 20, max_height - 2, max_width - 2)
        rectangle(w, round(max_height / 2) - 1, 1, max_height - 2, 20)

      elif section == 1:
        w.attron(curses.color_pair(2))
        rectangle(w, round(max_height / 2) - 1, 1, max_height - 2, 20)
        w.attroff(curses.color_pair(2))
        rectangle(w, 1, 1, round(max_height / 2) - 2, 20)
        rectangle(w, 1, 21, max_height - 5, max_width - 21)
        rectangle(w, max_height - 4, 21, max_height - 2, max_width - 21)
        rectangle(w, 1, max_width - 20, max_height - 2, max_width - 2)

      elif section == 2:
        w.attron(curses.color_pair(2))
        rectangle(w, 1, 21, max_height - 5, max_width - 21)
        w.attroff(curses.color_pair(2))
        rectangle(w, 1, 1, round(max_height / 2) - 2, 20)
        rectangle(w, max_height - 4, 21, max_height - 2, max_width - 21)
        rectangle(w, 1, max_width - 20, max_height - 2, max_width - 2)
        rectangle(w, round(max_height / 2) - 1, 1, max_height - 2, 20)

      elif section == 3:
        w.attron(curses.color_pair(2))
        rectangle(w, max_height - 4, 21, max_height - 2, max_width - 21)
        w.attroff(curses.color_pair(1))
        rectangle(w, 1, 1, round(max_height / 2) - 2, 20)
        rectangle(w, 1, 21, max_height - 5, max_width - 21)
        rectangle(w, 1, max_width - 20, max_height - 2, max_width - 2)
        rectangle(w, round(max_height / 2) - 1, 1, max_height - 2, 20)

      elif section == 4:
        w.attron(curses.color_pair(2))
        rectangle(w, 1, max_width - 20, max_height - 2, max_width - 2)
        w.attroff(curses.color_pair(2))
        rectangle(w, 1, 1, round(max_height / 2) - 2, 20)
        rectangle(w, 1, 21, max_height - 5, max_width - 21)
        rectangle(w, max_height - 4, 21, max_height - 2, max_width - 21)
        rectangle(w, round(max_height / 2) - 1, 1, max_height - 2, 20)

      # TEXT
      w.addstr(1, 2, "servers")
      w.addstr(round(max_height / 2) - 1, 2, "channels")
      w.addstr(1, max_width - 19, "members")
      w.addstr(1, 22, "messages")
      w.addstr(0, round(max_width / 2) - 6, "disline v0.1")
      w.addstr(max_height - 1, round(max_width / 2) - (3 + round(len(self.username) / 2)), "user: " + self.username)

  def servers_func(self, w, token, max_height, max_width, servers):
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
        self.active_server = index

      # SERVERS
      w.attron(curses.color_pair(2))
      rectangle(w, 1, 1, round(max_height / 2) - 2, 20)
      w.attroff(curses.color_pair(2))
      w.addstr(1, 2, "servers")
      for i, row in enumerate(servers):
        if i == index:
          w.attron(curses.color_pair(3))
          w.addstr(2 + i, 3, row['name'])
          w.attroff(curses.color_pair(3))

        else:
          if self.active_server == i:
            w.attron(curses.color_pair(2))
            w.addstr(2 + i, 3, row['name'])
            w.attroff(curses.color_pair(2))
          else:
            w.addstr(2 + i, 3, row['name'])

      # CONTENT CHANNELS
      if self.channels != None:
        if clear == False:
          w.clear()
          clear = True
        for i, channel in enumerate(self.channels):
          w.addstr(round(max_height / 2) + i, 3, channel['name'])

      # CHANNELS
      rectangle(w, round(max_height / 2) - 1, 1, max_height - 2, 20)
      w.addstr(round(max_height / 2) - 1, 2, "channels")

      # CONTENT
      rectangle(w, 1, 21, max_height - 5, max_width - 21)
      w.addstr(1, 22, "messages")
      
      # INPUT
      rectangle(w, max_height - 4, 21, max_height - 2, max_width - 21)
      
      # MEMBERS
      rectangle(w, 1, max_width - 20, max_height - 2, max_width - 2)
      w.addstr(1, max_width - 19, "members")

      w.addstr(0, round(max_width / 2) - 6, "disline v0.1")
      w.addstr(max_height - 1, round(max_width / 2) - (3 + round(len(self.username) / 2)), "user: " + self.username)

      w.refresh()

def main(w):
  # DISCORD VARIABLES
  token = "MzU4MzM3OTgxMjk3NDU5MjAx.G7Y7w4.jTSniiIo3wNu8KI64-rgB9TwiCCjj9iN93bLZI"
  channel_id = '982013142206931014'

  # COLOURS
  curses.init_pair(1, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
  curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLACK)
  curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)

  # MENU CONFIG
  max_height, max_width = w.getmaxyx()
  curses.curs_set(0)

  servers = curses.newwin(max_height - 4, 18, 2, 2)
  content = curses.newwin(max_height - 7, max_width - 43, 2, 22)
  messages = curses.newwin(1, max_width - 43, max_height - 3, 22)
  users = curses.newwin(max_height - 4, 17, 2, max_width - 19)

  # MAIN LOOP
  init(w, max_height, max_width)
  time.sleep(1)
  w.clear()
  servers_list = discord_servers.get_servers(token)
  sections_object = sections(servers, content, messages, users)

  while 1:
    sections_object.draw(w, max_height, max_width, servers_list, token)

    if sections_object.section_num == 0:
      sections_object.servers_func(w, token, max_height, max_width, servers_list)

  w.refresh()
  w.getch()

os.environ.setdefault('ESCDELAY', '25')
wrapper(main)