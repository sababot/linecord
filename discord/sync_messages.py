import messages as discord_messages
import time

def sync_msg(tui_object):
  while 1:
    time.sleep(0.1)

    if tui_object.token != None and tui_object.active_channel != None and len(tui_object.input_array) > 0 and tui_object.username != None:
      previous_messages = discord_messages.get_messages(tui_object.token, tui_object.active_channel["id"], 1)

      if tui_object.input_array[len(tui_object.input_array) - 1] != previous_messages[0]["author"]["username"] + ": " + previous_messages[0]["content"] and previous_messages[0]["author"]["username"] != tui_object.username:
        tui_object.input_array.append(previous_messages[0]["author"]["username"] + ": " + previous_messages[0]["content"])