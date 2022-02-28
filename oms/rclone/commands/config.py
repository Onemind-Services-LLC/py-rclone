from typing import Dict

from .abstracts import CommandAbstract


class Config(CommandAbstract):
	"""
	Wrapper for `rclone config`
	"""
	def __init__(self, obscure: bool = False):
		"""
		:param obscure: Declare passwords are plain and need obscuring
		"""
		super(Config, self).__init__()
		self.__obscure = obscure

	def create(self, name: str, parameters: Dict, remote_type: str) -> Dict:
		return self.cmd.rc(command="config/create", parameters={
			"name": name,
			"parameters": parameters,
			"type": remote_type,
			"opt": {"obscure": self.__obscure}
		})

	def delete(self, name: str) -> Dict:
		return self.cmd.rc(command="config/delete", parameters={"name": name})

	def get(self, name: str) -> Dict:
		return self.cmd.rc(command="config/get", parameters={"name": name})

	def list_remotes(self) -> Dict:
		return self.cmd.rc(command="config/listremotes")

	def password(self, name: str, parameters: Dict) -> Dict:
		return self.cmd.rc(command="config/password", parameters={"name": name, "parameters": parameters})

	def providers(self) -> Dict:
		return self.cmd.rc(command="config/providers")

	def update(self, name: str, parameters: Dict) -> Dict:
		return self.cmd.rc(command="config/update", parameters={"name": name, "parameters": parameters})
