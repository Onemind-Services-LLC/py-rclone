from typing import Dict

from .abstracts import CommandAbstract


class FsCache(CommandAbstract):
	"""
	Wrapper for `rclone fscache`
	"""

	def clear(self) -> Dict:
		return self.cmd.rc(command="fscache/clear")

	def entries(self) -> Dict:
		return self.cmd.rc(command="fscache/entries")
