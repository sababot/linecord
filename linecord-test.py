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
sys.path.insert(0, "./tui")
import custom
import sections

def main(w):
  # DISCORD VARIABLES
  token = "MzU4MzM3OTgxMjk3NDU5MjAx.GUVsqK.2_WkGNCho310ol9mOLIgZyERRoYGd-y8vVmZkg"

  # COLOURS
  curses.init_pair(1, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
  curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLACK)
  curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)

  # UI INIT
  max_height, max_width = w.getmaxyx()
  curses.curs_set(0)
  key = None

  # DISCORD INIT
  servers = [ {"name": "discdone", "id": "196", "expand": False},
              {"name": "dislinetest", "id": "256", "expand": False},
              {"name": "pussypalace", "id": "675", "expand": False},
              {"name": "test server", "id": "256", "expand": False}]

  channels = [ {"server_id": "196", "server_channels": ["general dungeon", "programming", "gaming", "village hall", "second test"]},
              {"server_id": "256", "server_channels": ["temple", "fitness", "rocket league"]},
              {"server_id": "675", "server_channels": ["linux", "setups", "meditation", "okay boom"]},
              {"server_id": "933", "server_channels": ["fair", "sock", "tennis bed"]}]

  ## MAIN LOOP
  custom.init(w, max_height, max_width)
  time.sleep(1.5)
  w.clear()

  user_interface = sections.tui(max_width, max_height, servers, channels)

  while 1:
    if key == 9 and user_interface.servers_toggle == True:
      user_interface.servers_toggle = False
    elif key == 9 and user_interface.servers_toggle == False:
      user_interface.servers_toggle = True

    elif (key == curses.KEY_DOWN or key == 106) and user_interface.servers_toggle == True:
      user_interface.active_channel["index"] += 1
    elif (key == curses.KEY_UP or key == 107) and user_interface.servers_toggle == True:
      user_interface.active_channel["index"] -= 1

    elif key in {curses.KEY_ENTER, 10, 13}:
      user_interface.enter(w)

    user_interface.select(w, curses)

    key = w.getch()

    w.refresh()
    w.clear()

os.environ.setdefault('ESCDELAY', '0')
wrapper(main)