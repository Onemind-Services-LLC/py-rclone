import logging

from .common import Command

logger = logging.getLogger(__name__)


class CommandAbstract:
	def __init__(self):
		self.cmd = Command()
