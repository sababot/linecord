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
  # COLOURS
  curses.init_pair(1, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
  curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLACK)
  curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)
  curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_BLACK)

  # TUI VAR INIT
  max_height, max_width = w.getmaxyx()
  curses.curs_set(0)
  key = None

  # DISCORD INIT
  token = "MzU4MzM3OTgxMjk3NDU5MjAx.Gg0stf.ZKdKhkq3cXbEdUflFilRDQJI5X1mLc9f1L_gQM"

  servers = [ {'id': '788450662915637258', 'name': 'sababox', 'icon': '77e8153f0e8051f7b4e83afe9442c608', 'owner': False, 'permissions': '1071698660929', 'features': [], "expand": False},
              {'id': '982619741497737258', 'name': 'test_server', 'icon': None, 'owner': True, 'permissions': '4398046511103', 'features': [], "expand": False}]

  channels = [[{'id': '788450662915637260', 'type': 4, 'name': 'vibe station', 'position': 1, 'flags': 0, 'parent_id': None, 'guild_id': '788450662915637258', 'permission_overwrites': []},
              {'id': '788450662915637261', 'type': 4, 'name': 'VC', 'position': 2, 'flags': 0, 'parent_id': None, 'guild_id': '788450662915637258', 'permission_overwrites': []},
              {'id': '788450663490387988', 'last_message_id': None, 'type': 2, 'name': 'General', 'position': 0, 'flags': 0, 'parent_id': '788450662915637261', 'bitrate': 64000, 'user_limit': 0, 'rtc_region': None, 'guild_id': '788450662915637258', 'permission_overwrites': [], 'rate_limit_per_user': 0, 'nsfw': False}, 
              {'id': '788453974201597952', 'last_message_id': '980253925955473438', 'type': 0, 'name': 'announcements', 'position': 0, 'flags': 0, 'parent_id': '788454495465635851', 'topic': None, 'guild_id': '788450662915637258', 'permission_overwrites': [], 'rate_limit_per_user': 0, 'nsfw': False},
              {'id': '788454225205657600', 'last_message_id': '909425305163276298', 'type': 0, 'name': 'vibing-chat', 'position': 4, 'flags': 0, 'parent_id': '788450662915637260', 'topic': None, 'guild_id': '788450662915637258', 'permission_overwrites': [], 'rate_limit_per_user': 0, 'nsfw': False},
              {'id': '788454495465635851', 'type': 4, 'name': 'welcome', 'position': 0, 'flags': 0, 'parent_id': None, 'guild_id': '788450662915637258', 'permission_overwrites': []},
              {'id': '802853064712650773', 'last_message_id': '964543068403539998', 'type': 0, 'name': '🥰motivation', 'position': 8, 'flags': 0, 'parent_id': '788454495465635851', 'topic': None, 'guild_id': '788450662915637258', 'permission_overwrites': [], 'rate_limit_per_user': 0, 'nsfw': False},
              {'id': '812280713385869342', 'type': 4, 'name': 'Prototping bots', 'position': 4, 'flags': 0, 'parent_id': None, 'guild_id': '788450662915637258', 'permission_overwrites': [{'id': '788455963165589514', 'type': 0, 'allow': '1049600', 'deny': '0'},
              {'id': '788450662915637258', 'type': 0, 'allow': '0', 'deny': '1049600'}]},
              {'id': '812280797138124822', 'last_message_id': '815598886630326294', 'type': 0, 'name': 'mybotsrule', 'position': 9, 'flags': 0, 'parent_id': '812280713385869342', 'topic': None, 'guild_id': '788450662915637258', 'permission_overwrites': [{'id': '788450662915637258', 'type': 0, 'allow': '0', 'deny': '1048576'},
              {'id': '788455963165589514', 'type': 0, 'allow': '1049600', 'deny': '0'}], 'rate_limit_per_user': 0, 'nsfw': False},
              {'id': '980505121131728956', 'last_message_id': '982019416873115668', 'type': 0, 'name': 'token-harvesting', 'position': 11, 'flags': 0, 'parent_id': '812280713385869342', 'topic': None, 'guild_id': '788450662915637258', 'permission_overwrites': [{'id': '788455963165589514', 'type': 0, 'allow': '1049600', 'deny': '0'},
              {'id': '788450662915637258', 'type': 0, 'allow': '0', 'deny': '1048576'}], 'rate_limit_per_user': 0, 'nsfw': False},
              {'id': '982013142206931014', 'last_message_id': '983342116057014282', 'type': 0, 'name': 'disline', 'position': 12, 'flags': 0, 'parent_id': '812280713385869342', 'topic': None, 'guild_id': '788450662915637258', 'permission_overwrites': [{'id': '788455963165589514', 'type': 0, 'allow': '1049600', 'deny': '0'},
              {'id': '788450662915637258', 'type': 0, 'allow': '0', 'deny': '1048576'}], 'rate_limit_per_user': 0, 'nsfw': False}],

              [{'id': '982619742042988615', 'type': 4, 'name': 'Text Channels', 'position': 0, 'flags': 0, 'parent_id': None, 'guild_id': '982619741497737258', 'permission_overwrites': []},
              {'id': '982619742042988616', 'type': 4, 'name': 'Voice Channels', 'position': 0, 'flags': 0, 'parent_id': None, 'guild_id': '982619741497737258', 'permission_overwrites': []},
              {'id': '982619742042988617', 'last_message_id': '983065866260336711', 'type': 0, 'name': 'general', 'position': 0, 'flags': 0, 'parent_id': '982619742042988615', 'topic': None, 'guild_id': '982619741497737258', 'permission_overwrites': [], 'rate_limit_per_user': 0, 'nsfw': False},
              {'id': '982619742508580864', 'last_message_id': None, 'type': 2, 'name': 'General', 'position': 0, 'flags': 0, 'parent_id': '982619742042988616', 'bitrate': 64000, 'user_limit': 0, 'rtc_region': None, 'guild_id': '982619741497737258', 'permission_overwrites': [], 'rate_limit_per_user': 0, 'nsfw': False}]]

  ## MAIN LOOP INIT
  custom.init(w, max_height, max_width)
  time.sleep(1.5)
  w.clear()

  # LOGIN

  # MAIN
  user_interface = sections.tui(max_width, max_height, token, servers, channels)

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
    pass

os.environ.setdefault('ESCDELAY', '0')
wrapper(main)