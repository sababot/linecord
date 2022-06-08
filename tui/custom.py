def init(w, max_height, max_width):
  w.addstr(round(max_height / 2) - 5, round(max_width / 2) - 29, " ___                                               __")
  w.addstr(round(max_height / 2) - 4, round(max_width / 2) - 29, "/\_ \    __                                       /\ \ ")
  w.addstr(round(max_height / 2) - 3, round(max_width / 2) - 29, "\//\ \  /\_\    ___      __    ___    ___   _ __  \_\ \ ")
  w.addstr(round(max_height / 2) - 2, round(max_width / 2) - 29, "  \ \ \ \/\ \ /' _ `\  /'__`\ /'___\ / __`\/\`'__\/'_` \ ")
  w.addstr(round(max_height / 2) - 1, round(max_width / 2) - 29, "   \_\ \_\ \ \/\ \/\ \/\  __//\ \__//\ \L\ \ \ \//\ \L\ \ ")
  w.addstr(round(max_height / 2), round(max_width / 2) - 29, "   /\____\\ \_\ \_\ \_\ \____\ \____\ \____/\ \_\\ \___,_\ ")
  w.addstr(round(max_height / 2) + 1, round(max_width / 2) - 29, "   \/____/ \/_/\/_/\/_/\/____/\/____/\/___/  \/_/ \/__,_ /")
  w.addstr(round(max_height / 2) + 2, round(max_width / 2) - 29, "                                               by sababot")
  w.refresh()

def vert_line(w, x, y1, y2):
  for i in range(y2 - y1):
    w.addstr(y1 + i, x, "│")