import yaml
import socket
import fcntl
import struct

from json import dumps as json_dumps
import pdb

class _Config(object):

    def __init__(self, config_path):
        assert isinstance(config_path, str)
        self._config_path = config_path
        self._config = None

    @property
    def config(self):
        if self._config is None:
            self._read_config()
        return self._config

    @config.setter
    def config(self, value):
        self._config = value

    def __getitem__(self, item):
            return self._config[item]


class YamlReader(_Config):

    def _read_config(self):

        with open(self._config_path, 'r') as config_file:
            content = config_file.read()
            self._config = yaml.load(content)

    def __str__(self):
        return json_dumps(self._config, indent=4)
