from curses.textpad import Textbox, rectangle
import custom

import sys
sys.path.insert(0, "../discord")
import messages as discord_messages
import servers as discord_servers
import channels as discord_channels

class tui:
  def __init__(self, max_width, max_height, token, servers, channels):
    self.max_width = max_width
    self.max_height = max_height

    self.token = token
    self.username = discord_messages.get_username(self.token)["username"]

    self.servers_toggle = True
    self.select_channel = {"index": 2, "type": "server", "local_index": None}
    self.input_string = ""
    self.input_array = []

    self.active_channel = None

    self.servers = servers
    self.select_server_index = 0
    self.active_server = None
    self.active_server_member_count = None

    self.channels = channels

  def select(self, w, curses):
    if self.servers_toggle == True:
      curses.curs_set(0)
      # OUTLINE
      custom.v_line(w, self.max_width - 25, 0, self.max_height)

      w.addstr(1, self.max_width - 23, "servers")

      for i in range(len(self.servers)):                            # get channels before a specific channel
        prev = 2
        for j in range(i, 0, -1):
          if self.servers[j - 1]["expand"] == True:
            prev += len(self.channels[j - 1])

        if self.servers[i]["expand"] == True:                       # section expanded
          # SERVERS
          if i + prev == self.select_channel["index"]:              # print selected server name
            w.attron(curses.color_pair(3))
            w.addstr(i + prev, self.max_width - 19, self.servers[i]["name"])
            w.attroff(curses.color_pair(3))

            if i != len(self.servers) - 1:
              w.addstr(i + prev, self.max_width - 23, "├──")
            else:
              w.addstr(i + prev, self.max_width - 23, "└──")

            self.select_channel["local_index"] = i
            self.select_channel["type"] = "server"
          else:                                                     # print non-selected server name
            w.addstr(i + prev, self.max_width - 19, self.servers[i]["name"])
            if i != len(self.servers) - 1:
              w.addstr(i + prev, self.max_width - 23, "├──")
            else:
              w.addstr(i + prev, self.max_width - 23, "└──")

          # CHANNELS
          for j in range(len(self.channels[i])): # print channels
            if j == len(self.channels[i]) - 1:
              if j + (i + 1) + prev == self.select_channel["index"]:
                w.addstr(j + (i + 1) + prev, self.max_width - 19, "└──")
                if i != len(self.servers) - 1:
                  w.addstr(j + (i + 1) + prev, self.max_width - 23, "│")
                w.attron(curses.color_pair(3))
                w.addstr(j + (i + 1) + prev, self.max_width - 15, self.channels[i][j]["name"])
                w.attroff(curses.color_pair(3))

                self.select_channel["local_index"] = j
                self.select_channel["type"] = "channel"
                self.select_server_index = i

              else:
                w.addstr(j + (i + 1) + prev, self.max_width - 19, "└──")
                w.addstr(j + (i + 1) + prev, self.max_width - 15, self.channels[i][j]["name"])
                if i != len(self.servers) - 1:
                  w.addstr(j + (i + 1) + prev, self.max_width - 23, "│")
            else:
              if j + (i + 1) + prev == self.select_channel["index"]:
                w.addstr(j + (i + 1) + prev, self.max_width - 19, "├──")
                if i != len(self.servers) - 1:
                  w.addstr(j + (i + 1) + prev, self.max_width - 23, "│")
                w.attron(curses.color_pair(3))
                w.addstr(j + (i + 1) + prev, self.max_width - 15, self.channels[i][j]["name"])
                w.attroff(curses.color_pair(3))

                self.select_channel["local_index"] = j
                self.select_channel["type"] = "channel"
                self.select_server_index = i
              else:
                w.addstr(j + (i + 1) + prev, self.max_width - 19, "├──")
                w.addstr(j + (i + 1) + prev, self.max_width - 15, self.channels[i][j]["name"])
                if i != len(self.servers) - 1:
                  w.addstr(j + (i + 1) + prev, self.max_width - 23, "│")
        else:                                                        # section not expanded
          # SERVERS
          if i + prev == self.select_channel["index"]:               # print selected server name
            w.attron(curses.color_pair(3))
            w.addstr(i + prev, self.max_width - 19, self.servers[i]["name"])
            w.attroff(curses.color_pair(3))

            if i != len(self.servers) - 1:
              w.addstr(i + prev, self.max_width - 23, "├──")
            else:
              w.addstr(i + prev, self.max_width - 23, "└──")

            self.select_channel["local_index"] = i
            self.select_channel["type"] = "server"
          else:                                                      # print non-selected server name
            w.addstr(i + prev, self.max_width - 19, self.servers[i]["name"])
            if i != len(self.servers) - 1:
              w.addstr(i + prev, self.max_width - 23, "├──")
            else:
              w.addstr(i + prev, self.max_width - 23, "└──")

  def input(self, w, curses, key):
    if self.servers_toggle == False:
      curses.curs_set(1)

      custom.h_line(w, self.max_height - 2, 2, self.max_width - 2)

      if key != None and key != -1 and key != 9 and key != 127 and key not in {curses.KEY_ENTER, 10, 13} and len(self.input_string) < self.max_width - 4:
        self.input_string += chr(key)
      elif key == 127:
        self.input_string = self.input_string[:-1]

      w.addstr(self.max_height - 1, 2, self.input_string)

    else:
      custom.h_line(w, self.max_height - 2, 2, self.max_width - 25)
      w.addstr(self.max_height - 1, 2, self.input_string)

  def enter(self, w):
    if self.servers_toggle == True:
      if self.select_channel["type"] == "server":
        if self.servers[self.select_channel["local_index"]]["expand"] == False:
          self.servers[self.select_channel["local_index"]]["expand"] = True

        elif self.servers[self.select_channel["local_index"]]["expand"] == True:
          self.servers[self.select_channel["local_index"]]["expand"] = False

      elif self.select_channel["type"] == "channel":
        self.active_channel = self.channels[self.select_server_index][self.select_channel["local_index"]]
        
        previous_messages = discord_messages.get_messages(self.token, self.active_channel["id"], 25)
        self.input_array = []
        for i in range(len(previous_messages) - 1, -1, -1):
          self.input_array.append(previous_messages[i]["author"]["username"] + ": " + previous_messages[i]["content"])

    elif self.servers_toggle == False and self.input_string != "":
      discord_messages.send_message(self.token, self.active_channel["id"], self.input_string)

      previous_messages = discord_messages.get_messages(self.token, self.active_channel["id"], 1)
      self.input_array.append(self.username + ": " + self.input_string)

      self.input_string = ""

  def content(self, w):
    if self.servers_toggle == False:
      custom.h_line(w, 0, 0, self.max_width - 1)
    else:
      custom.h_line(w, 0, 0, self.max_width - 25)

    if len(self.input_array) <= self.max_height - 3:
      for i in range(len(self.input_array)):
        w.addstr(i + 1, 2, self.input_array[i])

    else:
      for i in range(len(self.input_array) - (self.max_height - 3), len(self.input_array)):
        w.addstr((i - (len(self.input_array) - (self.max_height - 3))) + 1, 2, self.input_array[i])