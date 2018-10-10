import os
import sublime
import sublime_plugin
 

class CmderCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		#your cmder path
		CmderExeFile = "C:\\cmder_mini\\Cmder.exe"
		CmderExePath = "C:\\cmder_mini\\"
		os.chdir(CmderExePath)
		os.startfile(CmderExeFile)        
