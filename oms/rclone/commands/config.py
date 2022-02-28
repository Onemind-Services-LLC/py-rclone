import logging
from typing import Dict

from .common import Command

logger = logging.getLogger(__name__)


class Config:
	"""
	Wrapper for `rclone config`
	"""

	def __init__(self, obscure: bool = False):
		"""
		:param obscure: Declare passwords are plain and need obscuring
		"""
		self.__cmd = Command()
		self.__obscure = obscure

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

	def create(self, name: str, parameters: Dict, remote_type: str) -> Dict:
		return self.__cmd.rc(command="config/create", parameters={
			"name": name,
			"parameters": parameters,
			"type": remote_type,
			"opt": {"obscure": self.__obscure}
		})

	def delete(self, name: str) -> Dict:
		return self.__cmd.rc(command="config/delete", parameters={"name": name})

	def get(self, name: str) -> Dict:
		return self.__cmd.rc(command="config/get", parameters={"name": name})

	def list_remotes(self) -> Dict:
		return self.__cmd.rc(command="config/listremotes")

	def password(self, name: str, parameters: Dict) -> Dict:
		return self.__cmd.rc(command="config/password", parameters={"name": name, "parameters": parameters})

	def providers(self) -> Dict:
		return self.__cmd.rc(command="config/providers")

	def update(self, name: str, parameters: Dict) -> Dict:
		return self.__cmd.rc(command="config/update", parameters={"name": name, "parameters": parameters})
