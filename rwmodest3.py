import sublime
import sublime_plugin

import os
import sys
import stat

class WriteCommand(sublime_plugin.TextCommand):
        def run(self, edit):
                File = self.view.file_name()
                os.chmod(File, stat.S_IWUSR)
 
class ReadCommand(sublime_plugin.TextCommand):
        def run(self, edit):
                File = self.view.file_name()
                os.chmod(File, stat.S_IRUSR)
