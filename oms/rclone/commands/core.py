from typing import Dict, Optional, List

from .abstracts import CommandAbstract


class Core(CommandAbstract):
	"""
	Wrapper for `rclone core`
	"""

	def bwlimit(self, rate: Optional[str] = None) -> Dict:
		return self.cmd.rc(command="core/bwlimit", parameters={"rate": rate})

	def command(self, command: str, arg: List, opt: Dict, return_type: Optional[str] = "COMBINED_OUTPUT") -> Dict:
		return self.cmd.rc(
			command="core/command", parameters={"command": command, "arg": arg, "opt": opt, "returnType": return_type})

	def gc(self) -> Dict:
		return self.cmd.rc(command="core/gc")

	def group_list(self) -> Dict:
		return self.cmd.rc(command="core/group-list")

	def memstats(self) -> Dict:
		return self.cmd.rc(command="core/memstats")

	def obscure(self, clear: str) -> Dict:
		return self.cmd.rc(command="core/obscure", parameters={"clear": clear})

	def pid(self) -> Dict:
		return self.cmd.rc(command="core/pid")

	def quit(self, exit_code: Optional[int] = 0) -> Dict:
		return self.cmd.rc(command="core/quit", parameters={"exitCode": exit_code})

	def stats(self, group: Optional[str] = None) -> Dict:
		return self.cmd.rc(command="core/stats", parameters={"group": group})

	def stats_delete(self, group: Optional[str] = None) -> Dict:
		return self.cmd.rc(command="core/stats-delete", parameters={"group": group})

	def stats_reset(self, group: Optional[str] = None) -> Dict:
		return self.cmd.rc(command="core/stats-reset", parameters={"group": group})

	def transferred(self, group: Optional[str] = None) -> Dict:
		return self.cmd.rc(command="core/transferred", parameters={"group": group})

	def version(self) -> Dict:
		return self.cmd.rc(command="core/version")
