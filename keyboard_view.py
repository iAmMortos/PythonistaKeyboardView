from keyboard_panel import KeyboardPanel

import ui
import sharedlibs
sharedlibs.add_path_for('view_swap')
from view_swap import ViewSwap

class KeyboardView (ui.View):
	
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		alpha_keys = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
		alpha_alts = ['QWERTYUIOP', 'ASDFGHJKL', 'ZXCVBNM']
		special_keys = ['1234567890', '-/:;()$&@"', '.,?!\'']
		special_alts = ['[]{}#%^*+=', '_\\|~<>€£¥•', '.,?!\'']
		
		self.panels = [KeyboardPanel(alpha_keys, alpha_alts), KeyboardPanel(special_keys, special_alts)]
		
		self.vs = ViewSwap(self)
		lb = ui.Label()
		lb.name = 'lb1'
		lb.text = 'Keyboard'
		lb.alignment = ui.ALIGN_CENTER
		lb.bg_color = '#c0ffb3'
		lb.flex = 'WH'
		lb.frame = self.frame
		self.add_subview(lb)
		
	def layout(self):
		pass
		
	def resize(self, frame):
		pass
