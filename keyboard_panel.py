
from keyboard_row import KeyboardRow
import ui

class KeyboardPanel (ui.View):
	
	def __init__(self, keys, alts):
		if len(keys) != len(alts):
			raise Exception('The number of items in the "keys" list must match the number of items in the "alts" list.')
		self.rows = [KeyboardRow(keys[i], alts[i]) for i in range(len(keys))]
		
	def resize(self, frame):
		pass
