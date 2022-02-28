from typing import Optional


class S3:
	"""
	Wrapper for S3 connection
	"""

	def __init__(
		self,
		endpoint: str,
		access_key_id: str,
		secret_access_key: str,
		region: Optional[str] = "",
		chunk_size: Optional[str] = "5Mi",
		copy_cutoff: Optional[str] = "4.656Gi",
		disable_checksum: Optional[bool] = False,
		force_path_style: Optional[bool] = False,
		max_upload_parts: Optional[int] = 10000,
		memory_pool_flush_time: Optional[str] = "1m0s",
		no_check_bucket: Optional[bool] = False,
		no_head: Optional[bool] = False,
		provider: Optional[str] = "",
		upload_concurrency: Optional[int] = 4,
		upload_cutoff: Optional[str] = "200Mi"
	):
		self.__remote_type = "s3"
		self.__access_key_id = access_key_id
		self.__chunk_size = chunk_size
		self.__copy_cutoff = copy_cutoff
		self.__disable_checksum = disable_checksum
		self.__endpoint = endpoint
		self.__force_path_style = force_path_style
		self.__max_upload_parts = max_upload_parts
		self.__memory_pool_flush_time = memory_pool_flush_time
		self.__no_check_bucket = no_check_bucket
		self.__no_head = no_head
		self.__provider = provider
		self.__region = region
		self.__secret_access_key = secret_access_key
		self.__upload_concurrency = upload_concurrency
		self.__upload_cutoff = upload_cutoff

	@property
	def parameters(self):
		return {
			"access_key_id": self.__access_key_id,
			"chunk_size": self.__chunk_size,
			"copy_cutoff": self.__copy_cutoff,
			"disable_checksum": self.__disable_checksum,
			"endpoint": self.__endpoint,
			"force_path_style": self.__force_path_style,
			"max_upload_parts": self.__max_upload_parts,
			"memory_pool_flush_time": self.__memory_pool_flush_time,
			"no_check_bucket": self.__no_check_bucket,
			"no_head": self.__no_head,
			"provider": self.__provider,
			"region": self.__region,
			"secret_access_key": self.__secret_access_key,
			"upload_concurrency": self.__upload_concurrency,
			"upload_cutoff": self.__upload_cutoff,
		}

	@property
	def remote_type(self):
		return self.__remote_type


class Minio(S3):
	def __init__(
		self,
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
	):
		super().__init__(
			access_key_id=access_key_id,
			chunk_size=chunk_size,
			copy_cutoff=copy_cutoff,
			disable_checksum=disable_checksum,
			force_path_style=True,
			endpoint=endpoint,
			max_upload_parts=max_upload_parts,
			memory_pool_flush_time=memory_pool_flush_time,
			no_check_bucket=no_check_bucket,
			no_head=no_head,
			provider="minio",
			region="",
			secret_access_key=secret_access_key,
			upload_concurrency=upload_concurrency,
			upload_cutoff=upload_cutoff
		)
