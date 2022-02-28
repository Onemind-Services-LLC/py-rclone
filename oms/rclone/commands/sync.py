from typing import Dict

from .abstracts import CommandAbstract


class Sync(CommandAbstract):
	"""
	Wrapper for `rclone sync`
	"""

	def copy(self, src_fs: str, dst_fs: str, create_empty_src_dirs: bool) -> Dict:
		return self.cmd.rc(
			command="sync/copy",
			parameters={"srcFs": src_fs, "dstFs": dst_fs, "createEmptySrcDirs": create_empty_src_dirs}
		)

	def move(self, src_fs: str, dst_fs: str, create_empty_src_dirs: bool, delete_empty_src_dirs: bool) -> Dict:
		return self.cmd.rc(
			command="sync/move",
			parameters={
				"srcFs": src_fs,
				"dstFs": dst_fs,
				"createEmptySrcDirs": create_empty_src_dirs,
				"deleteEmptySrcDirs": delete_empty_src_dirs
			})

	def sync(self, src_fs: str, dst_fs: str, create_empty_src_dirs: bool) -> Dict:
		return self.cmd.rc(command="sync/sync", parameters={
			"srcFs": src_fs,
			"dstFs": dst_fs,
			"createEmptySrcDirs": create_empty_src_dirs
		})
