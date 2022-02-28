from typing import Dict

from .abstracts import CommandAbstract


class Job(CommandAbstract):
	"""
	Wrapper for `rclone mount`
	"""

	def listmounts(self) -> Dict:
		return self.cmd.rc(command="mount/listmounts")

	def mount(self, fs: str, mount_point: str, mount_type: str, mount_opt: Dict, vfs_opt: Dict) -> Dict:
		return self.cmd.rc(
			command="mount/mount",
			parameters={
				"fs": fs,
				"mountPoint": mount_point,
				"mountType": mount_type,
				"mountOpt": mount_opt,
				"vfsOpt": vfs_opt
			})

	def stop(self, job_id: int) -> Dict:
		return self.cmd.rc(command="job/stop", parameters={"jobid": job_id})

	def types(self) -> Dict:
		return self.cmd.rc(command="mount/types")

	def unmount(self, mount_point: str) -> Dict:
		return self.cmd.rc(command="mount/unmount", parameters={"mountPoint": mount_point})

	def unmountall(self) -> Dict:
		return self.cmd.rc(command="mount/unmountall")
