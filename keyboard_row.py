
import ui
from keyboard_key import KeyboardKey

class KeyboardRow (ui.View):
	def __init__(self, keys, alts):
		if len(keys) != len(alts):
			raise Exception('The given key string must March the length of the given alts string.')
		self.keys = [KeyboardKey(keys[i], alts[i]) for i in range(len(keys))]
		
	def insert_before(self, key, idx):
		self.keys = self.keys[:idx] + [key] + self.keys[idx:]
		
	def insert_after(self, key, idx):
		self.keys = self.keys[:idx+1] + [key] + self.keys[idx+1:]
		
	def resize(self, frame):
		pass
