import sys
sys.path.insert(0, "../tui")
import custom

def get_token(w, curses, max_height, max_width, token):
	custom.init_text(w, max_height, max_width)

	token_win = curses.newwin(1, round(max_width * 0.75), round(max_height * 0.7), round(max_width * 0.125))
	
	curses.textpad.rectangle(w, round(max_height * 0.7) - 1, round(max_width * 0.125) - 1, round(max_height * 0.7) + 1, round(max_width * 0.885) - 1)
	w.refresh()

	token_input = curses.textpad.Textbox(token_win)
	curses.curs_set(1)
	token_input.edit()
	curses.curs_set(0)

	return token_input.gather()