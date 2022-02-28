import json
import logging
import os
import subprocess
from typing import List, Union, Optional, Dict, Any

from semver import VersionInfo

logger = logging.getLogger(__name__)

BINARY = "rclone"
MAJOR_MIN_VERSION = 1
MINOR_MIN_VERSION = 57


class Command:
	def __init__(self):
		if not self.__which(name=BINARY):
			raise Exception("rClone not found, exiting")

		# Make sure the minimum version is met
		version = self.version()

		if version.major < MAJOR_MIN_VERSION or version.minor < MINOR_MIN_VERSION:
			raise Exception(f"Minimum version {MAJOR_MIN_VERSION}.{MINOR_MIN_VERSION}.0 required, found {version}")

		self.__hostname = os.environ.get("RC_HOSTNAME", "localhost")
		self.__port = os.environ.get("RC_PORT", 5572)
		self.__username = os.environ.get("RC_USERNAME", None)
		self.__password = os.environ.get("RC_PASSWORD", None)

	def __execute(self, command: List) -> Any:
		self.__log("debug", f"{' '.join([c for c in command])}")
		process = subprocess.run(command, capture_output=True, text=True)

		if process.stderr != "":
			raise Exception(process.stderr)

		try:
			result = json.loads(process.stdout)
		except json.decoder.JSONDecodeError:
			result = process.stdout

		return result

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
		logger_prefix = "[Command]"

		if hasattr(logger, log_type):
			getattr(logger, log_type)(f"{logger_prefix} {message}")
		else:
			# Invalid `log_type` passed
			raise Exception(f"{logger_prefix} Invalid {log_type}!")

	def __which(self, name: str) -> str:
		self.__log("info", f"Finding binary: {name}")
		for path in os.getenv("PATH").split(os.path.pathsep):
			full_path = path + os.sep + name
			if os.path.exists(full_path):
				self.__log("info", f"Binary found at {full_path}")
				return full_path
		self.__log("error", f"Binary {name} not found")
		return ""

	def rc(self, command: str, parameters: Optional[Dict] = None) -> Dict:
		command_list = ["rclone", "rc", f"--rc-addr={self.__hostname}:{self.__port}"]

		# Add the username or password if available
		if self.__username:
			command_list.append(f"--rc-user={self.__username}")

		if self.__password:
			command_list.append(f"--rc-pass={self.__password}")

		# Add the command to the list
		command_list.append(command)

		if parameters:
			command_list.append("--json")
			command_list.append(json.dumps(parameters))
			return self.__execute(command=command_list)
		return self.__execute(command=command_list)

	def version(self) -> Union[VersionInfo, str]:
		"""
		:return: Returns semver compliant version
		"""
		version = self.__execute(command=[BINARY, "version"])
		# Parse the version
		return VersionInfo.parse(version.split("\n")[0].split(" ")[-1].lstrip("v"))
