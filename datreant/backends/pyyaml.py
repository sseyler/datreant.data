"""
Interface classes for YAML state files.

"""

import os
import sys
import fcntl
import pickle
import logging
import warnings
from functools import wraps

import yaml

import datreant
from .serial import TreantFileSerial


class TreantFileYAML(TreantFileSerial):

    def _deserialize(self, handle):
        return yaml.load(handle)

    def _serialize(self, record, handle):
        yaml.dump(record, handle)
