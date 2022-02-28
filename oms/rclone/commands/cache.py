import logging
from typing import Optional, Dict

from .common import Command

logger = logging.getLogger(__name__)


class Cache:
	"""
	Wrapper for `rclone cache`
	"""

	def __init__(self):
		self.__cmd = Command()

	@staticmethod
	def __log(log_type: str, message: str):
		"""
		This method is to log all actions with a standard format

		Args:
			log_type (str): This should always be one of `info`, `warning`, `error`, `critical` or `debug`
			message (str): Message that should be logged
		"""
		# Sanitize log_type
		log_type = log_type.lower()

		# Initialize logger string
		logger_prefix = "[Config]"

		if hasattr(logger, log_type):
			getattr(logger, log_type)(f"{logger_prefix} {message}")
		else:
			# Invalid `log_type` passed
			raise Exception(f"{logger_prefix} Invalid {log_type}!")

	def expire(self, remote: str, with_data: Optional[bool] = False) -> Dict:
		return self.__cmd.rc(command="cache/expire", parameters={"remote": remote, "withData": with_data})

	def fetch(self) -> Dict:
		return self.__cmd.rc(command="cache/fetch")

	def stats(self) -> Dict:
		return self.__cmd.rc(command="cache/stats")
