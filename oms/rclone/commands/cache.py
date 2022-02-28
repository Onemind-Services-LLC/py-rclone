from typing import Optional, Dict

from .abstracts import CommandAbstract


class Cache(CommandAbstract):
	"""
	Wrapper for `rclone cache`
	"""

	def expire(self, remote: str, with_data: Optional[bool] = False) -> Dict:
		return self.cmd.rc(command="cache/expire", parameters={"remote": remote, "withData": with_data})

	def fetch(self) -> Dict:
		return self.cmd.rc(command="cache/fetch")

	def stats(self) -> Dict:
		return self.cmd.rc(command="cache/stats")
