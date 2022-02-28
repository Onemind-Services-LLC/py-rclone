import logging
from typing import Dict, Optional

from .common import Command
from ..storage.s3 import Minio

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

	def __create(self, name: str, parameters: Dict, remote_type: str) -> Dict:
		return self.__cmd.rc(command="config/create", parameters={
			"name": name,
			"parameters": parameters,
			"type": remote_type,
			"opt": {"obscure": self.__obscure}
		})

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

	def create_minio(
		self,
		name: str,
		endpoint: str,
		access_key_id: str,
		secret_access_key: str,
		chunk_size: Optional[str] = "5Mi",
		copy_cutoff: Optional[str] = "4.656Gi",
		disable_checksum: Optional[bool] = False,
		max_upload_parts: Optional[int] = 10000,
		memory_pool_flush_time: Optional[str] = "1m0s",
		no_check_bucket: Optional[bool] = False,
		no_head: Optional[bool] = False,
		upload_concurrency: Optional[int] = 4,
		upload_cutoff: Optional[str] = "200Mi"
	) -> Dict:
		minio = Minio(
			access_key_id=access_key_id,
			chunk_size=chunk_size,
			copy_cutoff=copy_cutoff,
			disable_checksum=disable_checksum,
			endpoint=endpoint,
			max_upload_parts=max_upload_parts,
			memory_pool_flush_time=memory_pool_flush_time,
			no_check_bucket=no_check_bucket,
			no_head=no_head,
			secret_access_key=secret_access_key,
			upload_concurrency=upload_concurrency,
			upload_cutoff=upload_cutoff
		)
		return self.__create(name=name, parameters=minio.parameters, remote_type=minio.remote_type)

	def delete(self, name: str):
		return self.__cmd.rc(command="config/delete", parameters={"name": name})
