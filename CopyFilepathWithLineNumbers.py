import sublime, sublime_plugin
import datetime
import shutil
import os.path

class CopyFilepathWithLineNumbersCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        fileName = self.view.file_name()

        if fileName == None:
            sublime.error_message("You have to save the file first!")
            return

        (rowStart, colStart) = self.view.rowcol(self.view.sel()[0].begin())
        (rowEnd, colEnd)     = self.view.rowcol(self.view.sel()[0].end())

        result = fileName + ":" + (str)(rowStart + 1)

        if rowStart != rowEnd:
            # multiple selection
            result += "-" + (str)(rowEnd + 1)

        sublime.set_clipboard(result)
