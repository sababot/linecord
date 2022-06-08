import custom

class tui:
  def __init__(self, max_width, max_height, servers, channels):
    self.max_width = max_width
    self.max_height = max_height
    self.username = ""

    self.servers_toggle = True
    self.active_channel = {"index": 2, "type": "server", "local_index": None}

    self.servers = servers
    self.active_server = None
    self.active_server_member_count = None

    self.channels = channels

  def select(self, w, curses):
    if self.servers_toggle == True:
      custom.vert_line(w, 24, 1, self.max_height - 1)
      w.addstr(1, 1, "servers")

      for i in range(len(self.servers)):                            # get channels before a specific channel
        prev = 2
        for j in range(i, 0, -1):
          if self.servers[j - 1]["expand"] == True:
            prev += len(self.channels[j - 1]["server_channels"])

        if self.servers[i]["expand"] == True:                       # section expanded
          # SERVERS
          if i + prev == self.active_channel["index"]:              # print selected server name
            w.attron(curses.color_pair(3))
            w.addstr(i + prev, 4, " " + self.servers[i]["name"])
            w.attroff(curses.color_pair(3))

            if i != len(self.servers) - 1:
              w.addstr(i + prev, 1, "├──")
            else:
              w.addstr(i + prev, 1, "└──")

            self.active_channel["local_index"] = i
            self.active_channel["type"] = "server"
          else:                                                     # print non-selected server name
            w.addstr(i + prev, 4, " " + self.servers[i]["name"])
            if i != len(self.servers) - 1:
              w.addstr(i + prev, 1, "├──")
            else:
              w.addstr(i + prev, 1, "└──")

          # CHANNELS
          for j in range(len(self.channels[i]["server_channels"])): # print channels
            if j == len(self.channels[i]["server_channels"]) - 1:
              if j + (i + 1) + prev == self.active_channel["index"]:
                w.addstr(j + (i + 1) + prev, 5, "└── ")
                if i != len(self.servers) - 1:
                  w.addstr(j + (i + 1) + prev, 1, "│")
                w.attron(curses.color_pair(3))
                w.addstr(j + (i + 1) + prev, 8, self.channels[i]["server_channels"][j])
                w.attroff(curses.color_pair(3))

                self.active_channel["local_index"] = j
                self.active_channel["type"] = "channel"

              else:
                w.addstr(j + (i + 1) + prev, 5, "└── ")
                w.addstr(j + (i + 1) + prev, 8, self.channels[i]["server_channels"][j])
                if i != len(self.servers) - 1:
                  w.addstr(j + (i + 1) + prev, 1, "│")
            else:
              if j + (i + 1) + prev == self.active_channel["index"]:
                w.addstr(j + (i + 1) + prev, 5, "├── ")
                if i != len(self.servers) - 1:
                  w.addstr(j + (i + 1) + prev, 1, "│")
                w.attron(curses.color_pair(3))
                w.addstr(j + (i + 1) + prev, 8, self.channels[i]["server_channels"][j])
                w.attroff(curses.color_pair(3))

                self.active_channel["local_index"] = j
                self.active_channel["type"] = "channel"
              else:
                w.addstr(j + (i + 1) + prev, 5, "├── ")
                w.addstr(j + (i + 1) + prev, 8, self.channels[i]["server_channels"][j])
                if i != len(self.servers) - 1:
                  w.addstr(j + (i + 1) + prev, 1, "│")
        else:                                                        # section not expanded
          # SERVERS
          if i + prev == self.active_channel["index"]:               # print selected server name
            w.attron(curses.color_pair(3))
            w.addstr(i + prev, 4, " " + self.servers[i]["name"])
            w.attroff(curses.color_pair(3))

            if i != len(self.servers) - 1:
              w.addstr(i + prev, 1, "├──")
            else:
              w.addstr(i + prev, 1, "└──")

            self.active_channel["local_index"] = i
            self.active_channel["type"] = "server"
          else:                                                      # print non-selected server name
            w.addstr(i + prev, 4, " " + self.servers[i]["name"])
            if i != len(self.servers) - 1:
              w.addstr(i + prev, 1, "├── ")
            else:
              w.addstr(i + prev, 1, "└── ")

  def enter(self, w):
    if self.active_channel["type"] == "server" and self.servers[self.active_channel["local_index"]]["expand"] == False:
      self.servers[self.active_channel["local_index"]]["expand"] = True

    elif self.active_channel["type"] == "server" and self.servers[self.active_channel["local_index"]]["expand"] == True:
      self.servers[self.active_channel["local_index"]]["expand"] = False









