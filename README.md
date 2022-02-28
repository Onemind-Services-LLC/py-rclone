## Python client for rClone

A Python wrapper for [rClone](https://rclone.org/).

`rclone` must be already installed and discoverable in `$PATH`.

### Requirements

- rClone: Minimum version `v1.57.0`

### Usage

Traditionally `rClone` has been used as CLI tool. It provides integration for several providers out of the box. However, there hasn't been a good
SDK for programmatically use the features of `rClone`.

`py-rclone` utilises `rClone`'s capability to let a program to control it remotely using it's [Remote Control](https://rclone.org/rc/) feature.

Note: Make sure you have `rClone` running with `remote control` enabled.

#### Create Config

```python
from oms.rclone.commands.config import Config
from oms.rclone.storage.s3 import Minio

minio = Minio(access_key_id="foo", endpoint="play.minio.com", secret_access_key="bar")

config = Config()
config.create(name="minio", parameters=minio.parameters, remote_type=minio.remote_type)
```

