import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle
import time
import os
import threading

import sys
sys.path.insert(0, "./discord")
import messages as discord_messages
import servers as discord_servers
import channels as discord_channels
import sync_messages as discord_sync_messages

sys.path.insert(0, "./tui")
import custom
import sections

sys.path.insert(0, "./login")
import login as discord_login

def main(w):
  # COLOURS
  curses.init_pair(1, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
  curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLACK)
  curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)
  curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_BLACK)

  # TUI VAR INIT
  max_height, max_width = w.getmaxyx()
  curses.curs_set(0)
  key = None

  token = None

  # LOGIN
  try:
    while discord_messages.check_token(token) != 200:
      token = discord_login.get_token(w, curses, max_height, max_width, token)
  except:
    sys.exit()

  w.clear()

  # DISCORD INIT
  servers = discord_servers.get_servers(token)
  for i in range(len(servers)):
    servers[i]["expand"] = False

  channels = []
  for i in range(len(servers)):
    channels.append(discord_channels.get_channels(token, servers[i]["id"]))

  ## MAIN LOOP INIT
  curses.halfdelay(10)

  # LOGIN

  # MAIN
  user_interface = sections.tui(max_width, max_height, token, servers, channels)

  sync = threading.Thread(target=discord_sync_messages.sync_msg, args=(user_interface,))
  sync.start()

  try:
    while 1:
      if key == 9 and user_interface.servers_toggle == True:
        user_interface.servers_toggle = False
      elif key == 9 and user_interface.servers_toggle == False:
        user_interface.servers_toggle = True

      elif (key == curses.KEY_DOWN or key == 106) and user_interface.servers_toggle == True:
        user_interface.select_channel["index"] += 1
      elif (key == curses.KEY_UP or key == 107) and user_interface.servers_toggle == True:
        user_interface.select_channel["index"] -= 1

      elif key in {curses.KEY_ENTER, 10, 13}:
        user_interface.enter(w)

      user_interface.content(w)
      user_interface.input(w, curses, key)
      user_interface.select(w, curses)

      key = w.getch()

      w.refresh()
      w.clear()

  except KeyboardInterrupt:
    try:
      sync.join()
    except:
      pass
    pass

os.environ.setdefault('ESCDELAY', '0')
wrapper(main)