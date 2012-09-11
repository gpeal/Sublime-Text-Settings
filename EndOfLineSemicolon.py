import sublime, sublime_plugin

class EndOfLineSemicolonCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		for region in self.view.sel():
			if region.empty():
				line = self.view.line(region)
				self.view.insert(edit, line.end(), ';')
			
