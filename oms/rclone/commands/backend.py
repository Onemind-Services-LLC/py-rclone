from typing import Dict, List

from .abstracts import CommandAbstract


class Backend(CommandAbstract):
	"""
	Wrapper for `rclone backend`
	"""

	def command(self, command: str, fs: str, arg: List, opt: Dict) -> Dict:
		return self.cmd.rc(command="backend/command", parameters={"command": command, "fs": fs, "arg": arg, "opt": opt})
