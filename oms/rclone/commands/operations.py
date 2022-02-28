from typing import Dict, Optional

from .abstracts import CommandAbstract


class Operations(CommandAbstract):
	"""
	Wrapper for `rclone operations`
	"""

	def about(self, fs: str) -> Dict:
		return self.cmd.rc(command="operations/about", parameters={"fs": fs})

	def cleanup(self, fs: str) -> Dict:
		return self.cmd.rc(
			command="operations/cleanup",
			parameters={"fs": fs})

	def copy_file(self, src_fs: str, src_remote: str, dst_fs: str, dst_remote: str) -> Dict:
		return self.cmd.rc(
			command="operations/copyfile",
			parameters={"srcFs": src_fs, "srcRemote": src_remote, "dstFs": dst_fs, "dstRemote": dst_remote})

	def copy_url(self, fs: str, remote: str, url: str, auto_filename: Optional[bool] = False) -> Dict:
		return self.cmd.rc(
			command="operations/copyurl",
			parameters={"fs": fs, "remote": remote, "url": url, "autoFilename": auto_filename})

	def delete(self, fs: str) -> Dict:
		return self.cmd.rc(command="operations/delete", parameters={"fs": fs})

	def delete_file(self, fs: str, remote: str) -> Dict:
		return self.cmd.rc(command="operations/deletefile", parameters={"fs": fs, "remote": remote})

	def fs_info(self, fs: str) -> Dict:
		return self.cmd.rc(command="operations/fsinfo", parameters={"fs": fs})

	def list(self, fs: str, remote: str, opt: Optional[Dict] = None) -> Dict:
		return self.cmd.rc(command="operations/list", parameters={"fs": fs, "remote": remote, "opt": opt})

	def mkdir(self, fs: str, remote: str) -> Dict:
		return self.cmd.rc(command="operations/mkdir", parameters={"fs": fs, "remote": remote})

	def move_file(self, src_fs: str, src_remote: str, dst_fs: str, dst_remote: str) -> Dict:
		return self.cmd.rc(command="operations/movefile", parameters={
			"srcFs": src_fs,
			"srcRemote": src_remote,
			"dstFs": dst_fs,
			"dstRemote": dst_remote
		})

	def public_link(self, fs: str, remote: str, unlink: Optional[bool] = False, expire: Optional[str] = "1d") -> Dict:
		return self.cmd.rc(command="operations/publiclink", parameters={
			"fs": fs,
			"remote": remote,
			"unlink": unlink,
			"expire": expire
		})

	def purge(self, fs: str, remote: str) -> Dict:
		return self.cmd.rc(command="operations/purge", parameters={"fs": fs, "remote": remote})

	def rmdir(self, fs: str, remote: str) -> Dict:
		return self.cmd.rc(command="operations/rmdir", parameters={"fs": fs, "remote": remote})

	def rmdirs(self, fs: str, remote: str, leave_root: Optional[bool] = False) -> Dict:
		return self.cmd.rc("operations/rmdirs", parameters={"fs": fs, "remote": remote, "leaveRoot": leave_root})

	def size(self, fs: str) -> Dict:
		return self.cmd.rc("operations/size", parameters={"fs": fs})

	def stat(self, fs: str, remote: str, opt: Optional[Dict] = None) -> Dict:
		return self.cmd.rc(command="operations/stat", parameters={"fs": fs, "remote": remote, "opt": opt})

	def upload_file(self, fs: str, remote: str) -> Dict:
		return self.cmd.rc(command="operations/uploadfile", parameters={"fs": fs, "remote": remote})
