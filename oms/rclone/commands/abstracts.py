from abc import ABC

from .common import Command


class CommandAbstract(ABC):
	def __init__(self):
		self.cmd = Command()
