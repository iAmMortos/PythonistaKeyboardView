import ui
from keyboard_view import KeyboardView
import sharedlibs
sharedlibs.add_path_for('view_swap')
from view_swap import ViewSwap

if __name__ == '__main__':
	kbv = KeyboardView()
	v = ui.load_view()
	vs = ViewSwap(v)
	vs.swap('kb', kbv)
	v.present('sheet')
