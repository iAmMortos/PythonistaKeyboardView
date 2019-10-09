
import ui
from size_mode import SizeMode

class KeyboardKey(ui.View):
	def __init__(self, key, alt, mode=SizeMode.FILL):
		self.key = key
		self.alt = alt
		self.size_mode = mode
		
	def resize(self, frame):
		pass
