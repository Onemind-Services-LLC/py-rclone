from typing import Dict

from .abstracts import CommandAbstract


class Job(CommandAbstract):
	"""
	Wrapper for `rclone job`
	"""

	def list(self) -> Dict:
		return self.cmd.rc(command="job/list")

	def status(self, job_id: int) -> Dict:
		return self.cmd.rc(command="job/status", parameters={"jobid": job_id})

	def stop(self, job_id: int) -> Dict:
		return self.cmd.rc(command="job/stop", parameters={"jobid": job_id})
