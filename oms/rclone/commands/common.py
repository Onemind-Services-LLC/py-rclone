import json
import logging
import os
import subprocess
from typing import List, Union, Optional, Dict

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

	def __execute(self, command: List) -> [bool, List]:
		self.__log("debug", f"Executing {' '.join([c for c in command])}")
		process = subprocess.Popen(command, stdout=subprocess.PIPE, universal_newlines=True)
		result = []
		failed = False
		while True:
			output = process.stdout.readline()
			if output:
				result.append(output.strip())
			self.__log("info", output.strip())
			return_code = process.poll()
			if return_code is not None:
				self.__log("debug", f"Return Code: {return_code}")

			try:
				if return_code >= 1:
					# Process failed
					failed = True
					break
				if not return_code:
					# Process succeeded
					break
				if failed:
					# Immediately break the loop
					break
			except TypeError:
				continue
		return not failed, result

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

	def rc(self, command: str, parameters: Optional[Dict] = None):
		if parameters:
			_, result = self.__execute(command=["rclone", "rc", command, "--json", json.dumps(parameters)])
			return json.loads(result[0])

	def version(self) -> Union[VersionInfo, str]:
		"""
		:return: Returns semver compliant version
		"""
		success, version = self.__execute(command=[BINARY, "version"])
		if success:
			# Parse the version
			return VersionInfo.parse(version[0].split(" ")[-1].lstrip("v"))
		return ""
